from abc import ABC, abstractmethod
class DomainError(ABC, Exception):
    
    def __init__(self):
        Exception.__init__(self)
        self.message = self._errorMessage()
    
    @abstractmethod
    def errorCode(self) -> str:
        pass
    
    @abstractmethod
    def _errorMessage() -> str:
        pass
