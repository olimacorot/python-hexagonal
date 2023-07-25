from dimecom.src.services.domain.service import Service
from dimecom.src.services.domain.service_id import ServiceId
from dimecom.src.services.domain.service_code import ServiceCode
from dimecom.src.services.domain.service_name import ServiceName
from dimecom.src.services.domain.service_repository import ServiceRepository
from dimecom.src.services.application.create.service_creator_request import ServiceCreatorRequest

class ServiceCreator:

    def __init__(self, repository: ServiceRepository):
        self.__repository = repository

    def run(self, request: ServiceCreatorRequest):
        id = ServiceId(request.id())
        code = ServiceCode(request.code())
        name = ServiceName(request.name())
        
        service = Service(id, code, name)

        self.__repository.save(service)