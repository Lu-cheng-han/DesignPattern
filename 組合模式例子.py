from abc import ABC, abstractmethod

class Company(ABC):

    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def add(self, val:'Company'):
        pass

    @abstractmethod
    def remove(self,val:'Company'):
        pass

    @abstractmethod
    def display(self,val:int):
        pass

    @abstractmethod
    def lineofduty(self):
        pass

class FinanceDepartment(Company):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def add(self, val: Company):
        pass
    
    def remove(self, val: Company):
        pass

    def display(self, val: int):
        star = val * '-'
        print(f'{star}{self.name}')
    
    def lineofduty(self):
        print('處理財務工作')

class HumanResourcesDepartment(Company):

    def __init__(self, name) -> None:
        super().__init__(name)
    
    def add(self, val: Company):
        pass

    def remove(self, val: Company):
        pass

    def display(self, val: int):
        star = val * '-'
        print(f'{star}{self.name}')
    
    def lineofduty(self):
        print('處理人力資源工作')

class ConcreteCompany(Company):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.company_list = []
    
    def add(self, val:Company):
        self.company_list.append(val)
    
    def remove(self, val: Company):
        self.company_list.remove(val)
    
    def display(self, val: int):
        star = val * '-'
        print(f'{star}{self.name}')
        val += 2
        for i in self.company_list:
            i.display(val)

    def lineofduty(self):
        print('處理公司得大小事')
        for i in self.company_list:
            i.lineofduty()

if __name__ == "__main__":
    jijun = ConcreteCompany('精俊')
    resource = HumanResourcesDepartment('精俊人力資源部')
    finance = FinanceDepartment('精俊財務部門')
    jijun.add(resource)
    jijun.add(finance)
    jijun_2 = ConcreteCompany('精俊分公司')
    jijun_2_resource = HumanResourcesDepartment('精俊分公司人力資源部')
    jijun_2_finance = FinanceDepartment('精俊分公司財務部門')

    jijun_2.add(jijun_2_finance)
    jijun_2.add(jijun_2_resource)

    jijun.add(jijun_2)
    jijun.display(1)    

    jijun.lineofduty()
