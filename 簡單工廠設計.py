# 初學者
# print("請輸入數字A:")
# a = input()
# print("請輸入數字B:")
# b = input()
# print("輸入+、-、*、/")
# c = input()

# if c == '+':
#     print(int(a)+int(b))
# elif c == '-':
#     print(a-b)
# elif c == '*':
#     print(a*b)
# elif c == '/':
#     print(a/b)
# 進階版
# class Operation:

#     @classmethod
#     def get_result(cls,a,b,operate):
#         if operate == '+':
#             print(float(a) + float(b))
#         elif operate == '-':
#             print(float(a) - float(b))
#         elif operate == '*':
#             print(float(a) * float(b))
#         elif operate == '/':
#             print(float(a) / float(b))
        
# print("請輸入數字A:")
# a = input()
# print("請輸入數字B:")
# b = input()
# print("輸入+、-、*、/")
# c = input()
# Operation.get_result(a,b,c)
from abc import ABC, abstractmethod
#完整版分開+、
class Operation:
    _number_a = 0
    _number_b = 0

    def get_number_a(self):
        return self._number_a
    def set_number_a(self,a):
        self._number_a = a
    def get_number_b(self):
        return self._number_b
    def set_number_b(self,b):
        self._number_b = b
    @abstractmethod
    def get_result():
        pass

class OperationAdd(Operation):
    
    def get_result(self):
        return self._number_a  + self._number_b

class OperationMinus(Operation):
    
    def get_result(self):
        return float(self._number_a)  - float(self._number_b)
    
class OperationMul(Operation):
    
    def get_result(self):
        return self._number_a  * self._number_b
    
class OperationDiv(Operation):
    
    def get_result(self):
        if self._number_b == 0:
            print('除數不為0',flush=True)
            return 
        return self._number_a  / self._number_b

class OperationFactory:

   @classmethod
   def create_operate(cls,type:str):
        operate = None
        if type == '+':
            operate = OperationAdd()
        elif type == '-':
            operate = OperationMinus()  
        elif type == '*':   
            operate = OperationMul()
        elif type == '/':
            operate = OperationDiv()
        return operate
    
print("請輸入數字A:")
a = input()
print("請輸入數字B:")
b = input()
print("輸入+、-、*、/")
c = input()
oper = OperationFactory.create_operate(str(c))
oper.set_number_a(a)
oper.set_number_b(b)
print("result = ",oper.get_result())