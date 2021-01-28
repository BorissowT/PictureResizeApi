import unittest

from consumer_container.serialization_consumer.schema import response_schema
from consumer_container.db_consumer.database import session
# add consumer_container. to schema


class ResponseConsumerSerializationTest(unittest.TestCase):
    identifier = None
    image = None
    width = None
    height = None

    @classmethod
    def setUpClass(cls):
        cls.identifier = "127.0.0.1"
        cls.image = cls.fill_image()

    @staticmethod
    def fill_image():
        with open('tests/unit_tests/test_data/base64_unresized_picture.txt', 'r') as file:
            image = file.read().replace('\n', '')
            return image

    def fill_valid_data(self):
        width, height = 20, 20
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    def fill_negative_width(self):
        width, height = -1, 20
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    def fill_negative_height(self):
        width, height = 20, -1
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    def fill_big_width(self):
        width, height = 2001, 20
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    def fill_big_height(self):
        width, height = 20, 2001
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    def test_valid_request(self):
        data = self.fill_valid_data()
        self.assertFalse(response_schema.validate(data, session=session),
                         msg="Request schema doesn't validate legal data")

    @unittest.expectedFailure
    def test_negative_width(self):
        data = self.fill_negative_width()
        self.assertFalse(response_schema.validate(data, session=session),
                         msg="Request schema doesn't indicate negative width")

    @unittest.expectedFailure
    def test_negative_height(self):
        data = self.fill_negative_height()
        self.assertFalse(response_schema.validate(data, session=session),
                         msg="Request schema doesn't indicate negative height")

    @unittest.expectedFailure
    def test_big_width(self):
        data = self.fill_negative_height()
        self.assertFalse(response_schema.validate(data, session=session),
                         msg="Request schema doesn't indicate too big width")

    @unittest.expectedFailure
    def test_big_height(self):
        data = self.fill_negative_height()
        self.assertFalse(response_schema.validate(data, session=session),
                         msg="Request schema doesn't indicate too big height")

