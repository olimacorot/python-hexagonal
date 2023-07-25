from dimecom.src.services.domain import *
from dimecom.src.services.application.create.service_creator_request import ServiceCreatorRequest
from dimecom.tests.src.services.domain.service_id_mother import ServiceIdMother
from dimecom.tests.src.services.domain.service_code_mother import ServiceCodeMother
from dimecom.tests.src.services.domain.service_name_mother import ServiceNameMother

class ServiceMother:

    @staticmethod
    def create(id: ServiceId, code: ServiceCode, name: ServiceName) -> Service:
        return Service(id, code, name)
    
    @staticmethod
    def fromRequest(request: ServiceCreatorRequest) -> Service:
        return ServiceMother.create(
            ServiceIdMother.create(request.id()),
            ServiceCodeMother.create(request.code()),
            ServiceNameMother.create(request.name()),
        )

    @staticmethod
    def random() -> Service:
        return ServiceMother.create(
            ServiceIdMother.random(),
            ServiceCodeMother.random(),
            ServiceNameMother.random()
        )
