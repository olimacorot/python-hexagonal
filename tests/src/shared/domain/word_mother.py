from dimecom.tests.src.shared.domain.mother_creator import MotherCreator

class WordMother(object):
    @staticmethod
    def random() -> str:
        return MotherCreator.random().name()