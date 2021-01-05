import base64
import os
import sys
from io import BytesIO
from json import loads

from PIL import Image
from kafka import KafkaConsumer

from db_consumer.database import session
from serialization_consumer.schema import response_schema, ResponseSchema

kafka_broker = os.environ.get("KAFKA_BROKER")
topic_name = 'topic_test'
group_name = 'my-group-id'

for arg in sys.argv:
    if arg == "-container":
        topic_name = os.environ.get("KAFKA_TOPIC_NAME")
        group_name = os.environ.get("KAFKA_GROUP_NAME")
    if "-topic_name=" in arg:
        topic_name = arg.split("-topic_name=")[1]
    if "-group_id=" in arg:
        group_name = arg.split("-group_id=")[1]

print("consumer is listening to the '{0}' topic in {1} group".format(topic_name, group_name))

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[kafka_broker],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=group_name,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    data_json = event.value
    try:
        binary_image = base64.b64decode(data_json["image"])
        pil_image = Image.open(BytesIO(binary_image))
        resized_image = pil_image.resize((int(data_json["width"]), int(data_json["height"])))
        byte_stream = BytesIO()
        resized_image.save(byte_stream, format='PNG')
    except Exception as error:
        print(error)
    else:
        resized_img_str = base64.b64encode(byte_stream.getvalue())
        data_json["image"] = resized_img_str
        result = response_schema.load(data_json, session=session)
        session.add(result)
        session.commit()
        print("successfully created")



