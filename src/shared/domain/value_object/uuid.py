import uuid

class Uuid:

    def __init__(self, value: str):
        self.__ensureIsValidUuid(value)
        self.__value = value
    
    @staticmethod
    def random():
        return Uuid.__init__(uuid.uuid4())

    def value(self) -> str:
        return self.__value
    
    def __ensureIsValidUuid(self, id) -> None:
        try:
            uuid.UUID(str(id))
        except ValueError:
            return Exception(f"{self.__class__} does not allow the value {id}")
