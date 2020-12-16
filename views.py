from flask import render_template, send_from_directory

from app import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
