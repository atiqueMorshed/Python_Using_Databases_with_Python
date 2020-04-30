class myClass:
    x = 0
    name = ""

    def __init__(self, n):
        self.name = n
        print("==============================")
        print("Inside Constructor| ", self.name,": ", self.x)
        print("==============================")

    def mymethod(self):
        self.x = self.x + 1
        print("Self: ", self, "X: ", self.x)

    def __del__(self):
        print("==============================")
        print("Inside Destructor|:", self.name, ": ", self.x)
        print("==============================")


class1 = myClass("FirstClass")
class1.mymethod()
class1.mymethod()
class1.mymethod()

class2 = myClass("SecondClass")
class3 = myClass("ThirdClass")

class2.mymethod()
class3.mymethod()

class2.mymethod()
class3.mymethod()

class2.mymethod()
class3.mymethod()
