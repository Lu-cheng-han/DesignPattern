from abc import abstractmethod,ABC

class Component(ABC):
    _name : str

    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
    
    @abstractmethod
    def add(self,val: 'Component'):
        pass

    @abstractmethod
    def remove(self, val: 'Component'):
        pass

    @abstractmethod
    def display(self, val):
        pass

class Leaf(Component):

    def __init__(self, name) -> None:
        super().__init__(name)

    def display(self, val):
        display = '-' * val
        print(display + self._name)
    
    def add(self, val: Component):
        pass

    def remove(self, val: Component):
        pass

class Composite(Component):
    

    def __init__(self, name) -> None:
        super().__init__(name)
        self.component_list = []
  

    def add(self,val: Component):
        self.component_list.append(val)

    def remove(self, val: Component):
        self.component_list.remove(val)

    def display(self, val):
        display = '-' * val
        print(display + self._name)
        for i in self.component_list:
            i.display(val + 2)

if __name__ == "__main__":
    root = Composite('root')
    root.add(Leaf('Leaf A'))
    root.add(Leaf('Leaf B'))

    comp = Composite('Composite X')
    comp.add(Leaf('Leaf XA'))
    comp.add(Leaf('Leaf XB'))
    
    comp2 = Composite('Composite Xy')
    comp2.add(Leaf('ab'))
    comp2.add(Leaf('cb'))
    comp.add(comp2)
    root.add(comp)

    root.display(1)





















