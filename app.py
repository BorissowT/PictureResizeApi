from flask import Flask
app = Flask(__name__)

from views import *

if __name__ == '__main__':
    import os
    kafka_brocker = os.environ.get("KAFKA_BROKER")
    print(kafka_brocker)
    app.run(host='0.0.0.0')
# host='0.0.0.0'
# debug=True