from flask import render_template, send_from_directory, request, jsonify


#from kafka_client.kafka_producer import producer

from app import app

from service_functions import hash_id


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    data_json = request.json
    hashed_id = hash_id(request.remote_addr)
    data_json["hashed_id"] = hashed_id
    #producer.send('topic_test', value=data_json)
    return jsonify(), 201, {"Location": "/api/", "id": hashed_id}


@app.route('/api/<int:status_id>/', methods=["GET"])
def get_status(status_id):
    return "{}".format(status_id)


@app.errorhandler(500)
def render_server_error(error):
    print(request.url)
    print(error)
    return "Something wrong. We'll try to fix that. Promise", 500


@app.errorhandler(404)
def render_not_found(error):
    print(request.url)
    return error, 404
