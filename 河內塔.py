
#a是原本盤
#b是暫時盤
#c是目標盤
class Hw:

    def tower_of_hanoi(self,n,a,b,c):
        if n == 1:
            print(f'第{n}盤面，從{a}到{c}')
        else:
            self.tower_of_hanoi(n-1, a, c, b)
            print(f'第{n}盤面，從{a}到{b}')
            self.tower_of_hanoi(n-1,b,a,c)

def move(from_peg, to_peg):
    print(f"Move a disk from Peg {from_peg} to Peg {to_peg}")

if __name__ == "__main__":
    hw = Hw()
    hw.tower_of_hanoi(4,"A","B","C")
    # print("請輸入層數",flush=True)
    # a = input()

    # for i in range(int(a)):
    #     current_layer = i + 1
    #     print(f"{i+1}層 a到c")
    #     print(f"{i+1}層 a到b")
    #     print(f"{i+1}層 c到b")

    # print(f"{i+1}層 a到c")
