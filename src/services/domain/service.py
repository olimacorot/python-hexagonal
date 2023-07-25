from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.src.services.domain.service_code import ServiceCode
from hexagonal.src.services.domain.service_name import ServiceName

class Service(object):

    def __init__(self, id: ServiceId, code: ServiceCode, name: ServiceName):
        self.__id = id
        self.__code = code
        self.__name = name

    def id(self) -> ServiceId:
        return self.__id
    
    def code(self) -> ServiceCode:
        return self.__code
    
    def name(self) -> ServiceName:
        return self.__name


