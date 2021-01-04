import base64
import os
from io import BytesIO
from json import loads

from PIL import Image
from kafka import KafkaConsumer


kafka_broker = os.environ.get("KAFKA_BROKER")

topic_name = 'topic_test'

print("consumer is listening to {} topic".format(topic_name))

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[kafka_broker],
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
    try:
        resized_image = pil_image.resize((int(width), int(height)))
    except Exception as error:
        print(error)
    else:
        byte_stream = BytesIO()
        resized_image.save(byte_stream, format='PNG')
        img_str = base64.b64encode(byte_stream.getvalue())
        print(img_str)

    #TODO: push data to database


