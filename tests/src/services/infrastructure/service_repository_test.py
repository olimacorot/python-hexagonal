import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dimecom.tests.src.services.domain.service_mother import ServiceMother
from dimecom.tests.src.services.domain.service_id_mother import ServiceIdMother
from dimecom.src.services.infrastructure.mysql_service_repository import MysqlServiceRepository
import os
from dotenv import load_dotenv

load_dotenv()

class ServiceRepositoryTest(unittest.TestCase):
    
    def setUp(self) -> None:
        engeine = create_engine(
            'mysql://'
            f'{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}'
            f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'
        )
        Session = sessionmaker(bind=engeine)
        self.session = Session()
        return super().setUp()

    def test_it_should_save_a_service(self):
        repository = MysqlServiceRepository(self.session)
        service = ServiceMother.random()

        repository.save(service)
    
    def test_it_should_an_existing_service(self):
        repository = MysqlServiceRepository(self.session)
        service = ServiceMother.random()

        repository.save(service)
        search = repository.search(service.id())

        self.assertEqual(str(service.id().value()), search.id().value())
        self.assertEqual(service.code().value(), search.code().value())
        self.assertEqual(service.name().value(), search.name().value())

        
    def test_it_should_not_return_a_non_existing_service(self):
        repository = MysqlServiceRepository(self.session)

        self.assertIsNone(repository.search(ServiceIdMother.random()))

    def tearDown(self):
        self.session.execute("DELETE FROM services")
        self.session.commit()