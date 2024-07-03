def square(x):
    return x*x
print(square(8))

print(square)

ref1 = square

print(ref1)

print(ref1(10))