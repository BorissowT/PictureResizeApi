import datetime as dt
import os
import sys
from json import loads

from kafka import KafkaConsumer

from service_functions.serv_fun import resize_picture, serialize_data, add_to_db
from serialization_consumer.schema import response_schema
from db_consumer.database import session

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

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[kafka_broker],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=group_name,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("consumer is listening to the '{0}' topic in {1} group".format(topic_name, group_name))

for event in consumer:
    print("+++++++++process begins at {}+++++++++++".format(dt.datetime.now()))
    data_json = event.value
    not_valid = response_schema.validate(data_json, session=session)
    if not_valid:
        print("validation error: {}".format(not_valid))
    else:
        resize_picture(data_json)
        result = serialize_data(data_json)
        add_to_db(result)
        



