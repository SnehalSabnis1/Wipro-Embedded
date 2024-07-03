def sdecorator(f):
    def d(a,b):
        return "**{}**".format(f(a,b))
    return d

@sdecorator
def add(a,b):
    return a+b

print(add(2,3))