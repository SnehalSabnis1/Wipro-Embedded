numbers = [x for x in range(200)]

divisible_numbers = list(filter(lambda x: x%8==0,numbers))

print(divisible_numbers)

#List Comprension
nums = [x for x in range (200) if x%8==0]

print(nums)