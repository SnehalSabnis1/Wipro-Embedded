#multiple decorator function

def vdecorator(f):
    def d(name):
        return "<div>{}</div>".format(f(name))
    return d


def sdecorator(f):
    def d(name):
        return "<s>{}</s>".format(f(name))
    return d

@vdecorator
@sdecorator
def display(name):
    return f"Welcome {name} to python"

print(display('bob'))