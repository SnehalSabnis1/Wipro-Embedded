fruits = ['apple',"banana","mango","kiwi","cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
numbers = [2,3,5,8,10]
nums = [x**2 for x in numbers if x%2==0]
print(nums)