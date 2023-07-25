import json
from http import HTTPStatus
from hexagonal.tests.apps.backend.unit_test_base import UnitTestBase

class ServicesGetControllerTest(UnitTestBase):

    def test_it_should_return_ok_an_exiting_service(self):
        id = "1c09c0c6-3852-4b7e-9e7b-3058e8a01bed"

        endpoint = f"/services/{id}"
        body = {
            "code": "int5",
            "name": "internet 5 mg"
        }
        self.assertRequestWithBody(endpoint, json.dumps(body), HTTPStatus.CREATED)

        want = body
        want["id"] = id
        self.assertResponse(endpoint, HTTPStatus.OK, want)

    def test_it_should_return_error_service_not_exist(self):
        id = "7473823a-2074-4379-b552-0414200ae66f"
        endpoint = f"/services/{id}"
        want = {'message': f'The service {id} has not been found'}
        self.assertResponse(endpoint, HTTPStatus.BAD_REQUEST, want)
