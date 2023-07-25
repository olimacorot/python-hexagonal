from hexagonal.src.services.domain.service import Service
from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.src.services.domain.service_not_exist import ServiceNotExist
from hexagonal.src.services.domain.service_repository import ServiceRepository
from hexagonal.src.services.application.find.service_finder_response import ServiceFinderResponse

class ServiceFinder:
    
    def __init__(self, repository: ServiceRepository):
        self.__repository = repository
    
    def run(self, id: ServiceId) -> ServiceFinderResponse:
        service = self.__repository.search(id)

        if service == None:
            raise ServiceNotExist(id)
            
        
        return ServiceFinderResponse(
            service.id().value(),
            service.code().value(),
            service.name().value()
        )