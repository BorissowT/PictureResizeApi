from flask import render_template, request, jsonify


from kafka_client.kafka_producer import producer

from app import app

from service_functions import topic_name
from db.database import Response, session
from serialization.schema import response_schema, serialize_request


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    serialized_data = serialize_request(request)
    print("sending meassage to {}".format(topic_name))
    producer.send(topic_name, value=serialized_data)
    return jsonify(), 201, {"location": "/api/", "identifier": serialized_data["identifier"]}


@app.route('/api/<status_id>/', methods=["GET"])
def get_status(status_id):
    req = session.query(Response).filter(Response.Identifier == status_id).first()
    if req:
        serialized_data = response_schema.dump(req)
        return jsonify(serialized_data), 200, {"location": "/api/{}".format(status_id)}
    else:
        return {"status": "not found"}, 400, {"location": "/api/{}".format(status_id)}


@app.errorhandler(500)
def render_server_error(error):
    print(request.url)
    print(error)
    return "Something wrong. We'll try to fix that. Promise", 500


@app.errorhandler(404)
def render_not_found(error):
    print(request.url)
    return error, 404