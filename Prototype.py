from abc import ABC,abstractmethod
class ProtoTypeInterface(ABC):

    @abstractmethod
    def clone():
        pass
    
    