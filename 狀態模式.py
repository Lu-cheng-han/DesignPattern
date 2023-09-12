#original
# class Work:
  
#     def __init__(self) -> None:
#         self.hour : int = 0
#         self.work_finished : bool = False
    
#     def WritejProgram(self):
#         if self.hour < 12:
#             print(f"當前時間{self.hour}點上午工作,精神百倍",flush=True)
#         elif self.hour < 13:
#             print(f"當前時間{self.hour}點餓了,午飯:犯困,午休",flush=True)
#         elif self.hour < 17:
#             print(f"當前時間{self.hour}點下午狀態還不錯繼續努力",flush=True)
#         else:
#             if (self.work_finished):
#                 print(f"當前時間{self.hour}點下班回家了",flush=True)
#             else:
#                 if (self.hour) < 21:
#                     print(f"當前時間{self.hour}點加班喔疲累之極",flush=True)
#                 else:
#                     print(f"當前時間{self.hour}點不行了，睡著了",flush=True)

# if __name__ == "__main__":
#     worker = Work()
#     worker.hour = 22
#     worker.work_finished = 1
#     worker.WritejProgram()

#狀態模式
from abc import ABC, abstractmethod
from 狀態模式 import State
class Work:
    def __init__(self) -> None:
        self.hour : int = 0
        self.work_finished : bool = False
        self.current_state : State = ForenoonState()
    
    def WriteProgram(self):
        self.current_state.WriteProgram()
    
    def SetState(self, state: State):
        self.current_state = state
    
    
class State(ABC):

    @abstractmethod
    def WriteProgram(self, w:Work):
        pass

class ForenoonState(State):
    def WriteProgram(self, w: Work):
        if w.hour < 12:
            print(f"當前時間{w.hour}點上午工作,精神百倍",flush=True)
        else:
            


