import unittest

from api_container.serialization.schema import request_schema

# add api_container. to imports in tested folder(schema, app, database)


class RequestSerializationTest(unittest.TestCase):
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
        with open('tests/unit_tests/test_data/base64_picture.txt', 'r') as file:
            image = file.read().replace('\n', '')
            return image

    def fill_valid_data(self):
        width, height = 20, 20
        data = {"identifier": self.identifier, "image": self.image, "width": width, "height": height}
        return data

    @staticmethod
    def fill_negative_width():
        width, height = -20, 20
        data = {"identifier": identifier, "image": image, "width": width, "height": height}
        return data

    @staticmethod
    def fill_negative_height():
        width, height = 20, -20
        data = {"identifier": identifier, "image": image, "width": width, "height": height}
        return data

    @staticmethod
    def fill_big_width():
        width, height = 2001, 20
        data = {"identifier": identifier, "image": image, "width": width, "height": height}
        return data

    @staticmethod
    def fill_big_height():
        width, height = 20, 2001
        data = {"identifier": identifier, "image": image, "width": width, "height": height}
        return data

    def test_valid_request(self):
        data = self.fill_valid_data()
        self.assertFalse(request_schema.validate(data), msg="Request schema doesn't validate legal data")

    @unittest.expectedFailure
    def test_negative_width(self):
        data = self.fill_negative_width()
        self.assertFalse(request_schema.validate(data), msg="Request schema doesn't indicate negative width")

    @unittest.expectedFailure
    def test_negative_height(self):
        data = self.fill_negative_height()
        self.assertFalse(request_schema.validate(data), msg="Request schema doesn't indicate negative height")

    @unittest.expectedFailure
    def test_big_width(self):
        data = self.fill_negative_height()
        self.assertFalse(request_schema.validate(data), msg="Request schema doesn't indicate too big width")

    @unittest.expectedFailure
    def test_big_height(self):
        data = self.fill_negative_height()
        self.assertFalse(request_schema.validate(data), msg="Request schema doesn't indicate too big height")



