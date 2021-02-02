from api_container.views import app
import unittest


# add api_container. to imports in tested folder(schema, app, database, views)


class IndexTemplateTest(unittest.TestCase):
    url = "/"

    def test_template(self):
        tester = app.test_client(self)
        response = tester.get(self.url)
        self.assertEqual(response.status_code, 200) and \
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


class ResultTemplateTest(IndexTemplateTest):
    url = "result?id="


if __name__ == "__main__":
    unittest.main()
