from dimecom.src.services.domain.service_id import ServiceId
from dimecom.src.shared.domain.domain_error import DomainError

class ServiceNotExist(DomainError):

    def __init__(self, id: ServiceId):
        self.__id = id
        
        super().__init__()

    def errorCode(self) -> str:
        return 'service_not_exist'
    
    def _errorMessage(self) -> str:
        return f"The service {self.__id.value()} has not been found"