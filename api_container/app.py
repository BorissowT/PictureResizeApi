import os
import sys

from flask import Flask

from api_container.service_functions import set_app_params

app = Flask(__name__)


if __name__ == '__main__':
    app_args = set_app_params(sys.argv)
    debug = app_args["debug"]
    host = app_args["host"]
    from views import *
    app.run(debug=debug, host=host)
