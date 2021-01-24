import unittest

import kafka
from kafka.errors import NoBrokersAvailable
from kafka.producer import KafkaProducer

import os


class BrokerCredentialsTest(unittest.TestCase):
    kafka_broker = None
    producer = None
    consumer = None
    topic_name = 'topic_test'
    group_name = 'my-group-id'

    # @classmethod
    # def setUpClass(cls):
    #     cls.kafka_broker = os.environ.get("KAFKA_BROKER")
    #     cls.producer = KafkaProducer(
    #         bootstrap_servers=[cls.kafka_broker],
    #     )
    #     cls.consumer = KafkaConsumer(
    #         cls.topic_name,
    #         bootstrap_servers=[cls.kafka_broker],
    #         auto_offset_reset='earliest',
    #         enable_auto_commit=True,
    #         group_id=cls.group_name,
    #     )
    def connect_producer(self):
        producer = KafkaProducer(bootstrap_servers=[self.kafka_broker])
        return producer

    def test_if_kafka_broker_exists(self):
        self.kafka_broker = os.environ.get("KAFKA_BROKER")
        self.assertIsNotNone(self.kafka_broker,
                             msg="Environment variable for the broker bootstrap server is not specified")

    def test_if_connection_producer_can_be_created(self):
        self.kafka_broker = os.environ.get("KAFKA_BROKER")
        try:
            self.connect_producer()
        except AttributeError:
            self.fail("Wrong type of kafka_broker parameter")
        except Exception as e:
            self.fail("Connection to Broker server can't be set up: {}".format(e))



