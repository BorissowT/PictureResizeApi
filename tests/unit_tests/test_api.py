import unittest

from api_container.serialization.schema import request_schema


class RequestSerializationTest(unittest.TestCase):
    identifier = None
    image = None
    width = None
    height = None

    @staticmethod
    def fill_valid_data():
        identifier = "127.0.0.1"
        with open('tests/unit_tests/test_data/base64_picture.txt', 'r') as file:
            image = file.read().replace('\n', '')
        width = 100
        height = 100
        data = {"identifier": identifier, "image": image, "width": width, "height": height}
        return data

    def test_valid_request(self):
        data = self.fill_valid_data()
        print(request_schema.dump(data))



