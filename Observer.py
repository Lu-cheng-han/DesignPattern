from abc import ABC, abstractmethod


class Secretary:
    import Observer

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

class Observer(ABC):

    @abstractmethod
    def __init__(self, name:str, secretary:Secretary) -> None:
        self.name = name
        self.secretary = secretary

    @abstractmethod
    def update(self):
        pass

class StockObserver(Observer):
    
    def __init__(self, name:str, secretary:Secretary) -> None:
        super().__init__(name,secretary)
    
    def update(self):
        print(f"{self.secretary.action} {self.name} 關閉股票，繼續工作!")

class NBAObserver(Observer):
    
    def __init__(self, name:str, secretary:Secretary) -> None:
        super().__init__(name,secretary)
    
    def update(self):
        print(f"{self.secretary.action} {self.name} 關閉NBA，繼續工作!")

if __name__ == '__main__':
    
    tongzizhei = Secretary()
    Hank = NBAObserver(name = "Hank", secretary = tongzizhei)
    Lisa = StockObserver(name = "Lisa", secretary = tongzizhei)
    Lili =  StockObserver(name = "LiLi", secretary = tongzizhei)
    tongzizhei.attach(Hank)
    tongzizhei.attach(Lisa)
    tongzizhei.attach(Lili)

    tongzizhei.action = "老闆回來了"
    tongzizhei.remove(Lisa)
    tongzizhei.remove(Lili)
    tongzizhei.notify()