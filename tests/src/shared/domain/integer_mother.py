from dimecom.tests.src.shared.domain.mother_creator import MotherCreator

class IntegerMother(object):
    @staticmethod
    def random() -> str:
        return MotherCreator.random().unique.random_int(min=1, max=5)