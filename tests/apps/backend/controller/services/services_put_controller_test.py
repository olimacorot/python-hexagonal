import json
from http import HTTPStatus
from dimecom.tests.apps.backend.unit_test_base import UnitTestBase

class ServicesPutControllerTest(UnitTestBase):

    def test_return_status_201_ok(self):
        endpoint = "/services/1aab45ba-3c7a-4344-8936-78466eca77fa"
        body = json.dumps({
            "code": "int5",
            "name": "internet 5 mg"
        })

        self.assertRequestWithBody(endpoint, body, HTTPStatus.CREATED)
        
