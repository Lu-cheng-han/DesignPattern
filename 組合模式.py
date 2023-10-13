from abc import abstractclassmethod,ABC

class Component(ABC):
    _name : str

    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
    
    @abstractclassmethod
    def add(self,val: 'Component'):
        pass

    @abstractclassmethod
    def remove(self, val: 'Component'):
        pass

    @abstractclassmethod
    def display(self, val):
        pass

class Leaf(Component):

    def __init__(self, name) -> None:
        super().__init__(name)