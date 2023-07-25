import unittest
from unittest.mock import Mock
from hexagonal.src.services.domain import *
from hexagonal.tests.src.services.domain.service_mother import ServiceMother
from hexagonal.src.services.application.find.service_finder import ServiceFinder
from hexagonal.tests.src.services.domain.service_id_mother import ServiceIdMother

class ServiceFinderTest(unittest.TestCase):

    def test_it_should_return_an_exiting_service(self):
        service = ServiceMother.random()

        repository = Mock(spec=ServiceRepository)
        repository.search.return_value = service

        finder = ServiceFinder(repository)
        finder.run(service.id())

        repository.search.assert_called_once_with(service.id())
    
    def test_it_should_return_error_with_failed_id(self):
        respoitory = Mock(spec=ServiceRepository)
        respoitory.search.return_value = None

        finder = ServiceFinder(respoitory)

        id = ServiceId('some-id')
        with self.assertRaises(Exception):
            finder.run(id)

        respoitory.search.assert_called_once_with(id)
    
    def test_it_should_return_error_service_not_exist(self):
        respoitory = Mock(spec=ServiceRepository)
        respoitory.search.return_value = None

        finder = ServiceFinder(respoitory)

        id = ServiceIdMother.random()
        with self.assertRaises(ServiceNotExist):
            finder.run(id)

        respoitory.search.assert_called_once_with(id)

        

