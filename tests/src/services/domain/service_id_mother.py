from dimecom.src.services.domain.service_id import ServiceId
from dimecom.tests.src.shared.domain.uuid_mother import UuidMother

class ServiceIdMother(object):
    @staticmethod
    def create(value: str) -> ServiceId:
        return ServiceId(value)

    @staticmethod
    def random() -> ServiceId:
        return ServiceIdMother.create(UuidMother.random())