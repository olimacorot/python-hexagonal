from hexagonal.src.services.domain.service import Service
from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.src.services.domain.service_code import ServiceCode
from hexagonal.src.services.domain.service_name import ServiceName
from hexagonal.src.services.domain.service_repository import ServiceRepository
from hexagonal.src.services.application.create.service_creator_request import ServiceCreatorRequest

class ServiceCreator:

    def __init__(self, repository: ServiceRepository):
        self.__repository = repository

    def run(self, request: ServiceCreatorRequest):
        id = ServiceId(request.id())
        code = ServiceCode(request.code())
        name = ServiceName(request.name())
        
        service = Service(id, code, name)

        self.__repository.save(service)