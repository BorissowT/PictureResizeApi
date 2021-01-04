import hashlib
import time
import os

topic_name = "topic_test"


def hash_id(ip_address):
    time_of_request = time.time()
    id_concatenated = ip_address + str(time_of_request)
    hashed_id = hashlib.sha1(id_concatenated.encode('utf-8')).hexdigest()
    return hashed_id


def set_app_params(argv):
    debug = True
    host = "localhost"
    for arg in argv:
        if arg == "-container":
            host = "0.0.0.0"
            debug = False
            global topic_name
            topic_name = os.environ.get("KAFKA_TOPIC_NAME")
        if "-topic_name=" in arg:
            topic_name = arg.split("-topic_name=")[1]
    return {"debug": debug, "host": host}
