import unittest
import mysql.connector
import os
from requests import Session
import json

# this tests require api, broker and db parts to be running


def invalid_request_assertion(type_of_error):
    def outer_function(fill_invalid_data_function):
        def wrapper_function(self):
            fill_invalid_data_function(self)
            self.post_request()
            error_message = "{{'{error:}': ['Value must be greater than 0 and less than 2000 px']}}".format(
                error=type_of_error)
            self.assertEqual(self.response.headers["status"],
                             error_message)
            self.assertEqual(self.response.status_code, 400)
        return wrapper_function
    return outer_function


class RequestTest(unittest.TestCase):
    image = None
    width = None
    height = None
    session = Session()
    response = None
    json_data = None

    @staticmethod
    def fill_image():
        image = 'iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABrUlEQVR4nF2RvWtTURyGn985597bJlQjGiPoFknVRlChQwMdRAcduvRfELvopC661kVE1EU6ty4WHEUUEawF21JcQgTBjyGINUqlliTXm/PhEFPEd3qH9+EdHuFv0pmxaWPUrAthVIv8yLy/k5tr3Oa/mJ0mcklrOWZ7Aa2lpK1M319mXSual2t8WFxEf9lPxQD8mqnsg3Dc2rDDq6BeZoZrOajdW6K+oRlRDqMAIolPJrEuGi0kRhFcYKPUfi+eKlCIEiaTIU4gvDEAQ72tMsEs4Pw7RCoh5Gtr1RYRHLK9/qN3QOC5ASife9L8VBj7jlZHsLx9+PrW3c0DN87n8qgsBa0h7bIlMSvCi+0SXV8nP1LEWYgjaHevt3bnni0IUwjj4tnc5Xh6YZJHhnZvHBMV6Wz3v3suTKilVtEzf0VYxbNCQhnHHhGCQdRZkmGwGQTAqq+zwzczNFUMVQTQgOVx34Nwmiz9jHcdTFQhxI0zZvkwEZACCvD8xLA+EHcRnW/QJONg51Qsv0vAVQZKEqBLXSb41gemCmv/mF+1gHvFqHYcRbEXy0eEB4PBHx2WmIunbvRcAAAAAElFTkSuQmCC'
        return image

    def fill_valid_data(self):
        image = self.fill_image()
        width, height = 50, 50
        data = {"image": image, "width": width, "height": height}
        json_data = json.dumps(data)
        self.json_data = json_data

    def fill_negative_width(self):
        image = self.fill_image()
        width, height = -50, 50
        data = {"image": image, "width": width, "height": height}
        json_data = json.dumps(data)
        self.json_data = json_data

    def fill_negative_height(self):
        image = self.fill_image()
        width, height = 50, -50
        data = {"image": image, "width": width, "height": height}
        json_data = json.dumps(data)
        self.json_data = json_data

    def fill_overtop_height(self):
        image = self.fill_image()
        width, height = 50, 2001
        data = {"image": image, "width": width, "height": height}
        json_data = json.dumps(data)
        self.json_data = json_data

    def fill_overtop_width(self):
        image = self.fill_image()
        width, height = 2001, 50
        data = {"image": image, "width": width, "height": height}
        json_data = json.dumps(data)
        self.json_data = json_data

    def post_request(self):
        self.session.head('http://127.0.0.1:5000/api/')
        self.response = self.session.post(
            url='http://127.0.0.1:5000/api/',
            data=self.json_data,
            headers={
                "Content-Type": "application/json"
            }
        )

    def test_successful_status_code(self):
        self.fill_valid_data()
        self.post_request()
        self.assertEqual(self.response.status_code, 201)

    def test_bad_status_code(self):
        self.fill_overtop_height()
        self.post_request()
        self.assertEqual(self.response.status_code, 400)

    @invalid_request_assertion("width")
    def test_negative_width(self):
        self.fill_negative_width()

    @invalid_request_assertion("width")
    def test_overtop_width(self):
        self.fill_overtop_width()

    @invalid_request_assertion("height")
    def test_negative_height(self):
        self.fill_negative_height()

    @invalid_request_assertion("height")
    def test_overtop_height(self):
        self.fill_overtop_height()


if __name__ == "__main__":
    unittest.main()