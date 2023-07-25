from faker import Faker, Generator

class MotherCreator(object):
    faker: Faker = None

    @staticmethod
    def random() -> Faker:
        return MotherCreator.faker if MotherCreator.faker else Faker()