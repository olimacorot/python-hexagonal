import uuid

class UuidMother:
    @staticmethod
    def random() -> str:
        return uuid.uuid4()