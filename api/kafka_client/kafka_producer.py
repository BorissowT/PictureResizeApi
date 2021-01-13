from json import dumps
from kafka.producer import KafkaProducer
import os

kafka_broker = os.environ.get("KAFKA_BROKER")

producer = KafkaProducer(
    bootstrap_servers=[kafka_broker],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
