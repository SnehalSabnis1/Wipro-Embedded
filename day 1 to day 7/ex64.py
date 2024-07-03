from functools import reduce

numbers = [ x for x in range(1,20)]

total = reduce(lambda x,y: x+y,numbers)

print(total)