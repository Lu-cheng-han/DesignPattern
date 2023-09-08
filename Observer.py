from abc import ABC, abstractmethod
import Observer

class Subject(ABC):

    @abstractmethod
    def attach(self, observer:Observer):
        pass

    @abstractmethod
    def remove(self, observer:Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def state(self):
        pass

class Secretary(Subject):
    test: int = 0

    def __init__(self) -> None:
        self._observers = []
        self.action = ""
    
    def attach(self, observer:Observer):
        self._observers.append(observer)

    def remove(self, observer:Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
    
    def state(self):
        return self.action

class Observer(ABC):

    @abstractmethod
    def __init__(self, name:str, subject:Subject) -> None:
        self.name = name
        self.subject = subject

    @abstractmethod
    def update(self):
        pass

class StockObserver(Observer):
    
    def __init__(self, name:str, secretary:Secretary) -> None:
        super().__init__(name,secretary)
    
    def update(self):
        print(f"{self.subject.action} {self.name} 關閉股票，繼續工作!")

class NBAObserver(Observer):
    
    def __init__(self, name:str, secretary:Secretary) -> None:
        super().__init__(name,secretary)
    
    def update(self):
        print(f"{self.subject.action} {self.name} 關閉NBA，繼續工作!")

if __name__ == '__main__':
    
    # tongzizhei = Secretary()
    print(Secretary().test,flush=True)
    Secretary().test = 20
    print(Secretary().test,flush=True)

    print(Secretary().test,flush=True)
    ac =Secretary.test = 20
    print(Secretary().test,flush=True)
    # Hank = NBAObserver(name = "Hank", secretary = tongzizhei)
    # Lisa = StockObserver(name = "Lisa", secretary = tongzizhei)
    # Lili =  StockObserver(name = "LiLi", secretary = tongzizhei)
    # tongzizhei.attach(Hank)
    # tongzizhei.attach(Lisa)
    # tongzizhei.attach(Lili)

    # tongzizhei.action = "老闆回來了"
    # tongzizhei.remove(Lisa)
    # tongzizhei.remove(Lili)
    # tongzizhei.notify()