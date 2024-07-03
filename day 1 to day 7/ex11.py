list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.append(80)
print("elements of list:",list1)
print("size of list:",len(list1))

list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.extend((60,70,80))
print("elements of list:",list1)
print("size of list:",len(list1))

list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.extend("abc")
print("elements of list:",list1)

list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.insert(2,50)
print("elements of list:",list1)
print("size of list:",len(list1))

list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.insert(0,50)
print("elements of list:",list1)
print("size of list:",len(list1))

list1=[10,20,30,40]
print("elements of list:",list1)
print("size of list:",len(list1))
list1.insert(1,"abc")
print("elements of list:",list1)
print("size of list:",len(list1))

num=111
len=[]
while(num):
    r=num%10
    len.insert(0,r)
    num=num//10
print(len)

