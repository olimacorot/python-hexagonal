import abc

from hexagonal.src.services.domain.service import Service
from hexagonal.src.services.domain.service_id import ServiceId

class ServiceRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, service: Service) -> None:
        pass

    @abc.abstractmethod
    def search(self, id: ServiceId) -> Service:
        pass