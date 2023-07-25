from http import HTTPStatus
from dimecom.tests.apps.backend.unit_test_base import UnitTestBase

class HealthCheckGetControllerTest(UnitTestBase):
    
    def test_check_api_status(self):
        want = {"backend": "ok", "number": 1}
        self.assertResponse('/health-check', HTTPStatus.OK, want)
