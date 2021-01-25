import json
import os
import unittest
from json import loads

from kafka import KafkaConsumer
from kafka.producer import KafkaProducer


class BrokerCredentialsTest(unittest.TestCase):
    kafka_broker = None
    producer = None
    consumer = None
    topic_name = 'topic_unit_test'
    group_name = 'my-group-id'

    def connect_producer(self):
        producer = KafkaProducer(bootstrap_servers=[self.kafka_broker])
        return producer

    def connect_consumer(self):
        consumer = KafkaConsumer(
                self.topic_name,
                bootstrap_servers=[self.kafka_broker],
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id=self.group_name,
            )
        return consumer

    def test_if_kafka_broker_exists(self):
        self.kafka_broker = os.environ.get("KAFKA_BROKER")
        self.assertIsNotNone(self.kafka_broker,
                             msg="Environment variable for the broker bootstrap server is not specified")

    def test_if_connection_producer_can_be_created(self):
        self.kafka_broker = os.environ.get("KAFKA_BROKER")
        try:
            self.connect_producer()
        except AttributeError:
            self.fail("Wrong type of kafka_broker parameter (producer).")
        except Exception as e:
            self.fail("Connection (producer) to the broker server can't be set up: {}".format(e))

    def test_if_connection_consumer_can_be_created(self):
        self.kafka_broker = os.environ.get("KAFKA_BROKER")
        try:
            self.connect_consumer()
        except AttributeError:
            self.fail("Wrong type of kafka_broker parameter (consumer).")
        except Exception as e:
            self.fail("Connection (consumer) to the broker server can't be set up: {}".format(e))


class MessageBrokerTest(unittest.TestCase):
    kafka_broker = None
    producer = None
    consumer = None
    topic_name = 'topic_unit_test'
    group_name = 'my-group-id'

    @classmethod
    def setUpClass(cls):
        cls.kafka_broker = os.environ.get("KAFKA_BROKER")
        cls.producer = KafkaProducer(
            bootstrap_servers=[cls.kafka_broker],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        cls.consumer = KafkaConsumer(
            cls.topic_name,
            bootstrap_servers=[cls.kafka_broker],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=cls.group_name,
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

    def send_message_to_the_topic(self):
        self.producer.send(self.topic_name, value="UNIT_TEST")

    def read_test_message_from_topic(self):
        for event in self.consumer:
            return event.value

    def test_kafka_message(self):
        self.send_message_to_the_topic()
        self.assertEqual(self.read_test_message_from_topic(), {'UNIT_TEST': 'test'})


