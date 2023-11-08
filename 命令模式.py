from abc import ABC,abstractmethod

class AbstractCommand(ABC):

    @abstractmethod
    def execute(self, value: int):
        pass

    @abstractmethod
    def undo(self):
        pass

class AddHandler:
    num: int = 0
    value: int = 0
    undo_list: list = []

    def add(self,value: int):
        self.value = value
        self.num += self.value
        self.undo_list.append(value)
        return self.num
    
    def undo(self):
        if self.undo_list:
            undo_value = self.undo_list.pop()
            self.num -= undo_value
        return self.num
        # self.num -= self.value
        # return self.num

class AddCommand(AbstractCommand):
    add_handler = AddHandler()

    def execute(self, value: int):
        return self.add_handler.add(value)
    
    def undo(self):
        return self.add_handler.undo()

class CalculatorForm:
    command: AbstractCommand
    
    def set_command(self, command: AbstractCommand):
        self.command = command
    
    def compute(self,val:int):
        return  self.command.execute(val)

    def undo(self):
        return self.command.undo()

if __name__ == "__main__":
    calculator = CalculatorForm()
    add_command = AddCommand()
    calculator.set_command(add_command)
    # calculator.compute(5)
    # calculator.compute(10)
    print(calculator.undo())
    print(calculator.undo())