class A:
    def printString(self):
        print("from A")

class C:
    def printString(self):
        print("from C")

class B(A,C):
    pass

obj=B()
obj.printString()

##
class A:
    def printString(self):
        print("from A")

class C:
    def printString(self):
        print("from C")

class B(C,A):
    pass

obj=B()
obj.printString()

##
class E:
    def printString(self):
        print("from E")

class A:
    def printString(self):
        print("from A")

class C(E):
    pass

class B(C,A):
    pass

obj=B()
obj.printString()
print(B.__mro__)