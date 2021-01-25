from json import dumps
from kafka.producer import KafkaProducer
import os

kafka_broker = os.environ.get("KAFKA_BROKER")
producer = None


def set_up_a_producer():
    try:
        global producer
        producer = KafkaProducer(
            bootstrap_servers=[kafka_broker],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
    except Exception as error:
        print(error)
        set_up_a_producer()
    else:
        print("Api has been successfully connected to the broker")


set_up_a_producer()
