class ServiceCreatorRequest:

    def __init__(self, id: str, code: str, name: str):
        self.__id = id
        self.__code = code
        self.__name = name
    
    def id(self) -> str:
        return self.__id
    
    def code(self) -> str:
        return self.__code
    
    def name(self) -> str:
        return self.__name