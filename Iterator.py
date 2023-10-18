from abc import ABC, abstractmethod


class Iterator(ABC):

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def current_item(self):
        pass

class Aggregate(ABC):

    @abstractmethod
    def create_ireator(self):
        pass

class ConcreteIterator(Iterator):

    aggregate: Aggregate
    current: int = 0

    def __init__(self, aggregate: Aggregate) -> None:
        super().__init__()
        self.aggregate = aggregate

    def first(self):
        return self.aggregate.name_list[0]
    
    def next(self):
        ret = None
        if self.current < self.aggregate.count():
            ret = self.aggregate.name_list[self.current]
        
        self.current += 1
        return ret

    def is_done(self):
        if self.current == self.aggregate.count():
            return True
        else:
            return False
    
    def current_item(self):
        return self.aggregate.name_list[self.current]
        
class ConcreteAggregate(Aggregate):

    def __init__(self) -> None:
        super().__init__()
        self.name_list = []

    def create_ireator(self):
        return ConcreteIterator(self)

    def count(self):
        return len(self.name_list)

    def append_item(self, val):
        self.name_list.append(val)

    def index(self,index):
        return self.name_list[index]

if __name__ == "__main__":

    collection = ConcreteAggregate()
    collection.append_item('Hank')
    collection.append_item('Lisa')
    collection.append_item('Brain')
    collection.append_item('Bese')

    iterator = ConcreteIterator(collection)
    while not iterator.is_done():
        item = iterator.next()
        print(item)
