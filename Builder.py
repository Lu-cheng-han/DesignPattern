from abc import ABC, abstractmethod

class Product:

    def __init__(self) -> None:
        self._parts = []
        

    def add(self, part):
        self._parts.append(part)        

    def show(self):
        print(self._parts,flush=True)

class Buidler(ABC):

    @abstractmethod
    def BuildPartA(self):
        pass

    @abstractmethod
    def BuildPartB(self):
        pass
    
    @abstractmethod
    def GetResult(self):
        pass

class ConcreteBuilder1(Buidler):
    
    _product = Product()

    def BuildPartA(self):
        self._product.add("部件A")

    def BuildPartB(self):
        self._product.add("部件B")
    
    def GetResult(self):
        return self._product
    
class ConcreteBuilder2(Buidler):
    
    _product = Product()

    def BuildPartA(self):
        self._product.add("部件X")

    def BuildPartB(self):
        self._product.add("部件Y")
    
    def GetResult(self):
        return self._product

class Director:

    def Construct(self,builder:Buidler):
        builder.BuildPartA()
        builder.BuildPartB()
    
if __name__ == '__main__':

    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()
    director.Construct(b1) 
    p1 = b1.GetResult()
    p1.show()
    director.Construct(b2) 
    p2 = b2.GetResult()
    p2.show()
        


