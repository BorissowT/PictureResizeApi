import requests

import unittest


class IndexTemplateTest(unittest.TestCase):
    url = "/"
    code = 200

    def test_template(self):
        response = requests.get('http://localhost:5000{}'.format(self.url))
        self.assertEqual(response.status_code, self.code)
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")


class ResultTemplateTest(IndexTemplateTest):
    url = "/result?id="
    code = 200


class NotFoundTemplateTest(IndexTemplateTest):
    url = "/1"
    code = 404


if __name__ == "__main__":
    unittest.main()
