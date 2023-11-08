
from abc import ABC, abstractmethod
class Actor:
    type: str
    sex: str
    face: str
    costume: str
    hairstyle: str

    def set_type(self, val):
        self.type = val
    
    def get_type(self):
        return self.type
    
    def set_sex(self, val):
        self.sex = val
    
    def get_sex(self):
        return self.sex
    
    def set_face(self, val):
        self.face = val
    
    def get_face(self):
        return self.face

    def set_costume(self, val):
        self.costume = val
    
    def get_costume(self):
        return self.costume
    
    def set_hairstyle(self, val):
        self.hairstyle = val
    
    def get_hairstyle(self):
        return self.hairstyle

class ActorBuilder(ABC):
    actor = Actor()

    @abstractmethod
    def build_type(self):
        pass

    @abstractmethod
    def build_sex(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_costume(self):
        pass

    @abstractmethod
    def build_hairstyle(self):
        pass

    def create_actor(self):
        return self.actor

class HeroActorBuilder(ActorBuilder):


    def build_type(self):
        self.actor.set_type("hero")
    
    def build_sex(self):
        self.actor.set_sex("male")
    
    def build_face(self):
        self.actor.set_face("so handsome like me")
    
    def build_costume(self):
        self.actor.set_costume("盔甲")
    
    def build_hairstyle(self):
        self.actor.set_hairstyle("飄逸")
    
class Director:

    @staticmethod
    def construct(builder: ActorBuilder ) -> None:
        builder.build_type()
        builder.build_sex()
        builder.build_face()
        builder.build_costume()
        builder.build_hairstyle()
        return builder.create_actor()

if __name__ == "__main__":
    ab = HeroActorBuilder()
    hero_actor = Director.construct(ab)
    
    print(hero_actor.get_type())
    print(hero_actor.get_sex())
