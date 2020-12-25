import base64
import os
from io import BytesIO
from json import loads

from PIL import Image
from kafka import KafkaConsumer

kafka_brocker_port = os.environ.get("KAFKA_BROKER_PORT")

consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:{}'.format(kafka_brocker_port)],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    data_json = event.value
    base64_image = data_json["image"]
    width = data_json["width"]
    height = data_json["height"]
    binary_image = base64.b64decode(base64_image)
    pil_image = Image.open(BytesIO(binary_image))
    resized_image = pil_image.resize((width, height))
    byte_stream = BytesIO()
    resized_image.save(byte_stream, format='PNG')
    img_str = base64.b64encode(byte_stream.getvalue())
    #TODO: push data to database
