from hexagonal.src.services.domain.service_name import ServiceName
from hexagonal.tests.src.shared.domain.word_mother import WordMother

class ServiceNameMother:

    @staticmethod
    def create(value: str) -> ServiceName:
        return ServiceName(value)

    @staticmethod
    def random() -> ServiceName:
        return ServiceNameMother.create(WordMother.random())