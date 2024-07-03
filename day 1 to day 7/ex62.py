numbers = [x for x in range(25)]

def square(x):
    return x*x

square_numbers = list(map(square,numbers))

print(square_numbers)