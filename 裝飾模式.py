from abc import ABC, abstractmethod
class PersonInterface(ABC):
    
    @abstractmethod
    def show(self):
        pass

class Person(PersonInterface):
    
    def __init__(self,name) -> None:
        self.name = name
    
    def show(self):
        print(f'裝飾後的{self.name}')

class Finery(PersonInterface):
    component : PersonInterface
    
    def decorate(self, component):
        self.component = component

    def show(self):
        if self.component != None:
            self.component.show()

class TShirt(Finery):

    def show(self):
        print('大T Shirt')
        super().show()

class Sneakers(Finery):

    def show(self):
        print('球鞋')
        super().show()

if __name__ == "__main__":
    person = Person('Hank')
    t_shirt = TShirt()
    sneaker = Sneakers()
    t_shirt.decorate(person)
    sneaker.decorate(t_shirt)
    sneaker.show()







