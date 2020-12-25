from json import dumps
from kafka.producer import KafkaProducer
import os

kafka_brocker_port = os.environ.get("KAFKA_BROKER_PORT")

producer = KafkaProducer(
    bootstrap_servers=['localhost:{}'.format(kafka_brocker_port)],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
