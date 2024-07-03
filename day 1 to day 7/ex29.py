class A:
    def printString(self):
        print("from A")
class B(A):
    def displayString(self):
        print("from child method")
    def printString(self):
        print("from B")

obj = B()
obj.displayString()
obj.printString()

##
class A:
    def printString(self):
        print("from A")
class B(A):
    def displayString(self):
        print("from child method")
    def printString(self):
        super().printString()
        print("from B")

obj = B()
obj.displayString()
obj.printString()
