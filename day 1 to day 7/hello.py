def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

def subnum(a,b):
    return a-b

def modulonum(a,b):
    return a%b

def f(x):
    def g(y):
        return y*y
    return x+g(x)
