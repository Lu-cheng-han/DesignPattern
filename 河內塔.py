
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

if __name__ == "__main__":
    hw = Hw()
    hw.tower_of_hanoi(3,"A","B","C")