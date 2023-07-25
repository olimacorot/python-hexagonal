import unittest
from unittest.mock import Mock
from dimecom.tests.src.services.domain.service_mother import ServiceMother
from dimecom.src.services.domain.service_repository import ServiceRepository
from dimecom.src.services.application.create.service_creator import ServiceCreator
from dimecom.tests.src.services.application.create.service_creator_request_mother import ServiceCreatorRequestMother

class ServiceCreatorTest(unittest.TestCase):
    __repository: Mock = None

    def test_it_should_create_a_valid_service(self):
        repository = self._repository()
        repository.save.return_value = None
        creator = ServiceCreator(repository)

        request = ServiceCreatorRequestMother.random()
        service = ServiceMother.fromRequest(request)
        creator.run(request)
        repository.save.assert_called_once()
        #repository.save.assert_called_once_with(service)
    
    def _repository(self) -> Mock:
        return self.__repository if self.__repository else Mock(spec=ServiceRepository)
