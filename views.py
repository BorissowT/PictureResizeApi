from flask import render_template, send_from_directory, request

from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    data = request.json
    print(data)
    return render_template("index.html")


@app.route('/api/<int:status_id>/', methods=["GET"])
def get_status(status_id):
    return "{}".format(status_id)


@app.errorhandler(500)
def render_server_error(error):
    return "Something wrong", 500


@app.errorhandler(404)
def render_not_found(error):
    return "Wrong url", 404
