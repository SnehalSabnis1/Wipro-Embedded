class A:
    def printString(self):
        print("from A")
class B(A):
    pass

obj = B()
obj.printString()

##
class A:
    def printString(self):
        print("from A")
class B(A):
    def displayString(self):
        print("from child method")

obj = B()
obj.printString()
obj.displayString()

