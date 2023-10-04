from abc import ABC, abstractmethod

class Target:

    def Request(self):
        print("普通要求")

class Adaptee:
    
    def SpecificRequest(self):
        print("特殊要求")

class Adapter(Target):
    adaptee = Adaptee()

    def Request(self):
        self.adaptee.SpecificRequest()

class HeroInterface(ABC):

    @abstractmethod
    def attack(self):
        pass

class MyHero(HeroInterface):
    
    def attack(self):
        print("自家英雄攻擊")

class UnionHero:

    def touch(self):
        print("聯名英雄攻擊",flush=True)

class HeroAdapter(HeroInterface):
    union_hero = None

    def __init__(self, union: 'UnionHero') -> None:
        super().__init__()
        self.union_hero = union


    def attack(self):
        self.union_hero.touch()

if __name__ == "__main__":
    hero = MyHero()
    hero.attack()
    union = HeroAdapter(UnionHero())
    union.attack()
