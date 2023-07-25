class StringValueObject:
    def __init__(self, value: str):
        self.__value = value
    
    def value(self) -> str:
        return self.__value