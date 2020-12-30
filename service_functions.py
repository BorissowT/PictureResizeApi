import hashlib
import time


def hash_id(ip_address):
    time_of_request = time.time()
    id_concatenated = ip_address + str(time_of_request)
    hashed_id = hashlib.sha1(id_concatenated.encode('utf-8')).hexdigest()
    return hashed_id
