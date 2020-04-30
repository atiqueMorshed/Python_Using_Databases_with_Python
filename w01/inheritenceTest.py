class ParentClass:
    x = 0
    name = ""

    def __init__(self, n):
        self.name = n
        print("==============================")
        print("Inside Parent Constructor| ", self.name, "X: ", self.x)
        print("==============================")

    def mymethod(self):
        print("==============================")
        self.x = self.x + 1
        print(" mymethod : Self: ", self, "X: ", self.x)
        print("==============================")


    def __del__(self):
        print("==============================")
        print("Inside Parent Destructor|:", self.name, "X: ", self.x)
        print("==============================")


class ChildClass(ParentClass):
    y = 10

    def __init__(self, n):
        super().__init__(n)
        print("==============================")
        print("Inside Constructor| ", self.name, "Y: ", self.y)
        print("==============================")

    def childmethod(self):
        print("==============================")
        self.y = self.y + 1
        print(" childmethod : Self: ", self, "Y: ", self.y)
        self.mymethod()
        print("==============================")

    def __del__(self):
        print("==============================")
        print("Inside Child Destructor|:", self.name, "Y: ", self.y)
        print("==============================")


class1 = ChildClass("FirstClass")
class1.childmethod()
