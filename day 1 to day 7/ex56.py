def f():
    yield 1
    yield 2
    yield 3
    
    #return 1
    #return 2
    #return 3

for num in f():
    print(num)