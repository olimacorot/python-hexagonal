import pickle
from os.path import exists
from dimecom.src.services.domain.service import Service
from dimecom.src.services.domain.service_id import ServiceId
from dimecom.src.services.domain.service_repository import ServiceRepository

class FileServiceRepository(ServiceRepository):
    
    __FILE_PATH = "src/services/"

    def save(self, service: Service) -> None:
        with open(self.__fileName(service.id().value()), 'wb') as out_file:
            pickle.dump(service, out_file)
    
    def search(self, id: ServiceId) -> Service:
        if exists(self.__fileName(id.value())) == False:
            return None

        with open(self.__fileName(id.value()), 'rb') as in_file:
            service = pickle.load(in_file)
            return service
        
    def __fileName(self, id: str) -> str:
        return f'{self.__FILE_PATH}{id}.pkl'

