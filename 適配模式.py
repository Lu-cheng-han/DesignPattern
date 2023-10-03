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

if __name__ == "__main__":
    target = Adapter()
    target.Request()