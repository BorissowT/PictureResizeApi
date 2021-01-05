from flask import render_template, request, jsonify


from kafka_client.kafka_producer import producer

from app import app

from service_functions import hash_id, topic_name
from db.database import Request, session
from serialization.Schema import request_schema


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    data_json = request.json
    hashed_id = hash_id(request.remote_addr)
    data_json["identifier"] = hashed_id
    print("sending meassage to {}".format(topic_name))
    producer.send(topic_name, value=data_json)
    return jsonify(), 201, {"Location": "/api/", "id": hashed_id}


@app.route('/api/<status_id>/', methods=["GET"])
def get_status(status_id):
    req = session.query(Request).filter(Request.Identifier == status_id).first()
    serialized_data = request_schema.dump(req)
    return jsonify(serialized_data), 200, {"Location": "/api/{}".format(status_id)}


@app.errorhandler(500)
def render_server_error(error):
    print(request.url)
    print(error)
    return "Something wrong. We'll try to fix that. Promise", 500


@app.errorhandler(404)
def render_not_found(error):
    print(request.url)
    return error, 404
