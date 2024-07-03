#decorator function

def sdecorator(f):
    def d(name):
        return "<s>{}</s>".format(f(name))
    return d

@sdecorator
def display(name):
    return f"Welcome {name} to python"

print(display('bob'))