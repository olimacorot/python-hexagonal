from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.tests.src.shared.domain.uuid_mother import UuidMother

class ServiceIdMother(object):
    @staticmethod
    def create(value: str) -> ServiceId:
        return ServiceId(value)

    @staticmethod
    def random() -> ServiceId:
        return ServiceIdMother.create(UuidMother.random())