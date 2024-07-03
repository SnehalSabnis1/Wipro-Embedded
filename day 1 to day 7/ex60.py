numbers = [x for x in range(50)]

print(numbers)

def f(x):
    return x%2 == 0

even_numbers = list(filter(f,numbers))

print(even_numbers)