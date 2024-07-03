#nested function

def f(x):
    def g(y):
        return y*y
    return x+g(x)

val = f(10)
print(val)