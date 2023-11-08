from abc import ABC,abstractmethod


class PurchaseRequest:
    amount: float
    number: int
    purpose: str

    def __init__(self, amount:int, number:int, purpose: str) -> None:
        self.amount = amount
        self.number = number
        self.purpose = purpose
    
    def set_amount(self, val):
        self.amount = val
    
    def get_amount(self):
        return self.amount
    
    def set_number(self, val):
        self.number = val
    
    def get_number(self):
        return self.number
    
    def set_purpose(self, val):
        self.purpose = val
    
    def get_purpose(self):
        return self.purpose

class Approver(ABC):
    successor: 'Approver'
    name: str

    def __init__(self, name) -> None:
        self.name = name
    
    def set_successor(self, val:'Approver'):
        self.successor = val
    
    @abstractmethod
    def process_request(self, request: PurchaseRequest):
        pass

class Director(Approver):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def process_request(self, request: PurchaseRequest):
        if request.get_amount() < 50000:
            print("主任", self.name,"審批採購單",request.get_number(),request.get_amount())
        else:
            self.successor.process_request(request)

class VicePresident(Approver):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def process_request(self, request: PurchaseRequest):
        if request.get_amount() < 100000:
            print("副董事長:", self.name,"審批採購單:",request.get_number(),"金額:",request.get_amount())
        else:
            self.successor.process_request(request)

class President(Approver):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def process_request(self, request: PurchaseRequest):
        if request.get_amount() < 500000:
            print("董事長:", self.name,"審批採購單:",request.get_number(),"金額:",request.get_amount())
        else:
            self.successor.process_request(request)
    
class Congress(Approver):
    
    def __init__(self, name) -> None:
        super().__init__(name)

    def process_request(self, request: PurchaseRequest):
        print("董事會議審批採購單:", self.name,"審批採購單:",request.get_number(),"金額:",request.get_amount())
       
        
if __name__ == "__main__":
    
    wjzhang = Director("張無忌")
    gyang = VicePresident("楊過")
    jguo = President("郭靜")
    meeting = Congress("董事會")

    wjzhang.set_successor(gyang)
    gyang.set_successor(jguo)
    jguo.set_successor(meeting)

    pr1 = PurchaseRequest(45000,10001,"購買倚天劍")
    wjzhang.process_request(pr1)
    pr2 = PurchaseRequest(60000,10002,"葵花寶典")
    wjzhang.process_request(pr2)
    pr3 = PurchaseRequest(160000,10003,"金剛經")
    wjzhang.process_request(pr3)
