#closure function

def f(x):
    def g():
        print(x)
    g()

f(10)

##
def f(x):
    def g():
        return x*x
    return g

v = f(10)
print(v)
print(v())