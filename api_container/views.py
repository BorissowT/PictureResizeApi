from flask import render_template, request, jsonify


from kafka_client.kafka_producer import producer

from app import app

from service_functions import topic_name
from db.database import Response, session
from serialization.schema import response_schema, request_schema


@app.route("/", methods=["GET"])
def index_page():
    return render_template("index.html")


@app.route("/result", methods=["GET"])
def result_page():
    return render_template("result.html")


@app.route("/api/", methods=["POST"])
def post_new_picture():
    request.json["identifier"] = request.remote_addr
    valid = request_schema.validate(request.json)
    if valid:
        return jsonify(), 400, {"location": "/api/", "status": valid}
    serialized_data = request_schema.dump(request.json)
    print("sending meassage to {}".format(topic_name))
    producer.send(topic_name, value=serialized_data)
    return jsonify(), 201, {"location": "/api/", "identifier": serialized_data["identifier"]}


@app.route('/api/<status_id>/', methods=["GET"])
def get_by_status(status_id):
    response = session.query(Response).filter(Response.Identifier == status_id).first()
    session.close()
    if response:
        serialized_data = response_schema.dump(response)
        return jsonify(serialized_data), 200, {"location": "/api/{}".format(status_id)}
    else:
        return {"status": "not found"}, 202, {"location": "/api/{}".format(status_id)}


@app.errorhandler(500)
def render_server_error(error):
    print(request.url)
    print(error)
    return "Something wrong. We'll try to fix that. Promise", 500


@app.errorhandler(404)
def render_not_found(error):
    print(request.url)
    return error, 404
