from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from dimecom.src.services.domain.service import Service
from dimecom.src.services.domain.service_id import ServiceId
from dimecom.src.services.domain.service_code import ServiceCode
from dimecom.src.services.domain.service_name import ServiceName

Base = declarative_base()
class ServicesOrm(Base):
    __tablename__ = 'services'
    id = Column('id', String, primary_key=True)
    code = Column('code', String)
    name = Column('name', String)

    def mapper(self):
        return Service(
            ServiceId(self.id),
            ServiceCode(self.code),
            ServiceName(self.name)
        )