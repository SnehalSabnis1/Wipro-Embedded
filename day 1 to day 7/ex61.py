numbers = [x for x in range(50)]

print(numbers)

even_numbers = list(filter(lambda x: x%2==0,numbers))

print(even_numbers)