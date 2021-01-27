import unittest

from api_container.serialization.schema import request_schema, response_schema
from api_container.db.database import Response, session

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


class ResponseSerializationTest(unittest.TestCase):

    @staticmethod
    def add_test_picture_to_db():
        data = {'height': 12, 'width': 12, 'image': b'iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABrUlEQVR4nF2RvWtTURyGn985597bJlQjGiPoFknVRlChQwMdRAcduvRfELvopC661kVE1EU6ty4WHEUUEawF21JcQgTBjyGINUqlliTXm/PhEFPEd3qH9+EdHuFv0pmxaWPUrAthVIv8yLy/k5tr3Oa/mJ0mcklrOWZ7Aa2lpK1M319mXSual2t8WFxEf9lPxQD8mqnsg3Dc2rDDq6BeZoZrOajdW6K+oRlRDqMAIolPJrEuGi0kRhFcYKPUfi+eKlCIEiaTIU4gvDEAQ72tMsEs4Pw7RCoh5Gtr1RYRHLK9/qN3QOC5ASife9L8VBj7jlZHsLx9+PrW3c0DN87n8qgsBa0h7bIlMSvCi+0SXV8nP1LEWYgjaHevt3bnni0IUwjj4tnc5Xh6YZJHhnZvHBMV6Wz3v3suTKilVtEzf0VYxbNCQhnHHhGCQdRZkmGwGQTAqq+zwzczNFUMVQTQgOVx34Nwmiz9jHcdTFQhxI0zZvkwEZACCvD8xLA+EHcRnW/QJONg51Qsv0vAVQZKEqBLXSb41gemCmv/mF+1gHvFqHYcRbEXy0eEB4PBHx2WmIunbvRcAAAAAElFTkSuQmCC', 'identifier': '90778862599f2b95a5192261d168b141436b613f'}
        result = response_schema.load(data, session=session)
        session.add(Response(**result))
        session.commit()

    def serialize_orm_instance(self):
        response = session.query(Response).first()
        if response is None:
            self.add_test_picture_to_db()
            response = session.query(Response).first()
        serialized_data = response_schema.dump(response)
        return serialized_data

    def test_protected_identifier_attribute(self):
        serialized_data = self.serialize_orm_instance()
        self.assertFalse("Identifier" in serialized_data, msg="'Identifier' attribute is exposed!")

    def test_protected_width_attribute(self):
        serialized_data = self.serialize_orm_instance()
        self.assertFalse("Width" in serialized_data, msg="'Width' attribute is exposed!")

    def test_protected_height_attribute(self):
        serialized_data = self.serialize_orm_instance()
        self.assertFalse("Height" in serialized_data, msg="'Height' attribute is exposed!")

    def test_protected_image_attribute(self):
        serialized_data = self.serialize_orm_instance()
        self.assertFalse("BaseCode" in serialized_data, msg="'BaseCode' attribute is exposed!")