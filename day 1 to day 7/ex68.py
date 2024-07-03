#decorator function

def display(name):
    return f"Welcome {name} to python"

def sdecorator(f):
    def d(name):
        return "<s>{}</s>".format(f(name))
    return d

display = sdecorator(display)
print(display)
print(display('bob'))
