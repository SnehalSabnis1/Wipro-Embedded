list1=['a','b','c','d','e']
list2=list1
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))

list3=['a','b','c','d','e']
list4=['a','b','c','d','e']
print("reference of list1:",id(list3))
print("reference of list2:",id(list4))

print("reference of 1st element of list1:",id(list3[0]))
print("reference of 1st element of list2:",id(list4[0]))

list1=['a','b','c','d','e']
list2=list1
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))

list2[1]='m'
print("elements of list1:",list1)
print("elements of list2:",list2)

list1=['a','b','c','d','e']
list2=list1.copy()
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))

list1=['a','b','c','d','e']
list2=list1[:]
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))
print("elements of list1:",list1)
print("elements of list2:",list2)
print("reference of 2nd element of list1:",id(list1[1]))
print("reference of 2nd element of list2:",id(list2[1]))

list2[1]='g'
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))
print("elements of list1:",id(list1))
print("elements of list2:",id(list2))
print("reference of 2nd element of list1:",id(list1[2]))
print("reference of 2nd element of list2:",id(list2[2]))

list1=['a','b',['c','d'],'e']
list2=list1[:]
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))
print("elements of list1:",list1)
print("elements of list2:",list2)
print("reference of 3rd element of list1:",id(list1[2]))
print("reference of 3rd element of list2:",id(list2[2]))

print(list2[2][1])

list2[2][1]='g'
print("elements of list1:",list1)
print("elements of list2:",list2)
print("reference of 3rd element of list1:",id(list1[2]))
print("reference of 3rd element of list2:",id(list2[2]))

from copy import deepcopy
list1=['a','b',['c','d'],'e']
list2=deepcopy(list1)
print("reference of list1:",id(list1))
print("reference of list2:",id(list2))
print("elements of list1:",list1)
print("elements of list2:",list2)
print("reference of 3rd element of list1:",id(list1[2]))
print("reference of 3rd element of list2:",id(list2[2]))