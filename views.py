from flask import render_template, send_from_directory, request, jsonify

import base64
from PIL import Image
from io import BytesIO

from app import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    data_json = request.json
    base64_image = data_json["image"]
    binary_image = base64.b64decode(base64_image)
    pil_image = Image.open(BytesIO(binary_image))
    resized_image = pil_image.resize((300, 300))
    byte_stream = BytesIO()
    resized_image.save(byte_stream, format='PNG')
    img_str = base64.b64encode(byte_stream.getvalue())
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
