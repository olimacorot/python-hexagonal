from dimecom.src.services.domain import *
from dimecom.src.services.application.create.service_creator_request import ServiceCreatorRequest
from dimecom.tests.src.services.domain.service_id_mother import ServiceIdMother
from dimecom.tests.src.services.domain.service_code_mother import ServiceCodeMother
from dimecom.tests.src.services.domain.service_name_mother import ServiceNameMother

class ServiceCreatorRequestMother:

    @staticmethod
    def create(id: ServiceId, code: ServiceCode, name: ServiceName) -> ServiceCreatorRequest:
        return ServiceCreatorRequest(
            id.value(),
            code.value(),
            name.value()
        )
    
    @staticmethod
    def random() -> ServiceCreatorRequest:
        return ServiceCreatorRequestMother.create(
            ServiceIdMother.random(),
            ServiceCodeMother.random(),
            ServiceNameMother.random(),
        )
