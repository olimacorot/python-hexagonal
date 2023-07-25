import unittest
from dimecom.apps.backend.public.app import app, db

class UnitTestBase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def assertResponse(self, endpoint: str, expectedStatusCode: int, expectedResponse):
        response = self.app.get(endpoint, headers={"Content-Type": "application/json"})

        self.assertEqual(expectedStatusCode, response.status_code)
        self.assertEqual(expectedResponse, response.json)
    
    def assertRequestWithBody(self, endpoint: str, body, expectedStatusCode: int):
        response = self.app.put(
            endpoint,
            headers={"Content-Type": "application/json"},
            data=body
        )

        self.assertEqual(expectedStatusCode, response.status_code)
        self.assertEqual(None, response.json)
    
    def tearDown(self):
        with app.app_context():
            db.session.execute("DELETE FROM services")
            db.session.commit()