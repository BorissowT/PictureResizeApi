from flask import render_template, send_from_directory, request, jsonify


from kafka_client.kafka_producer import producer
from json import dumps
from app import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    data_json = request.json
    producer.send('topic_test', value=data_json)
    # TODO: return identifier
    return jsonify(), 201


@app.route('/api/<int:status_id>/', methods=["GET"])
def get_status(status_id):
    return "{}".format(status_id)


@app.errorhandler(500)
def render_server_error(error):
    return "Something wrong", 500


@app.errorhandler(404)
def render_not_found(error):
    return "Wrong url", 404
