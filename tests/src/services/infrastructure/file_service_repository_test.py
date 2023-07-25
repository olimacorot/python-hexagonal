import unittest
from hexagonal.tests.src.services.domain.service_mother import ServiceMother
from hexagonal.tests.src.services.domain.service_id_mother import ServiceIdMother
from hexagonal.src.services.infrastructure.file_service_repository import FileServiceRepository

class FileServiceRepositoryTest(unittest.TestCase):
    
    def test_it_should_save_a_service(self):
        repository = FileServiceRepository()
        service    = ServiceMother.random()

        repository.save(service)
    
    def test_it_should_an_existing_service(self):
        repository = FileServiceRepository()
        service    =  ServiceMother.random()

        repository.save(service)
        search = repository.search(service.id())
        self.assertEqual(service.id().value(), search.id().value())
        self.assertEqual(service.code().value(), search.code().value())
        self.assertEqual(service.name().value(), search.name().value())
        

    def test_it_should_not_return_a_non_existing_service(self):
        repository = FileServiceRepository()

        self.assertIsNone(repository.search(ServiceIdMother.random()))