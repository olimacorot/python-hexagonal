from dimecom.src.services.domain.service_code import ServiceCode
from dimecom.tests.src.shared.domain.word_mother import WordMother

class ServiceCodeMother:

    @staticmethod
    def create(value: str) -> ServiceCode:
        return ServiceCode(value)

    @staticmethod
    def random() -> ServiceCode:
        return ServiceCodeMother.create(WordMother.random())