from sqlalchemy.orm import Session
from hexagonal.src.services.domain.service import Service
from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.src.services.domain.service_repository import ServiceRepository
from hexagonal.src.services.infrastructure.mappings.services_orm import ServicesOrm

class MysqlServiceRepository(ServiceRepository):
    
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save(self, service: Service) -> None:
        serviceOrm = ServicesOrm(
            id=service.id().value(),
            code=service.code().value(),
            name=service.name().value(),
        )
        self.__session.add(serviceOrm)
        self.__session.flush()
        self.__session.commit()
    
    def search(self, id: ServiceId) -> Service:
        serviceOrm = self.__session.query(ServicesOrm).filter_by(id=id.value()).first()
        if None == serviceOrm:
            return None
        
        return serviceOrm.mapper()
