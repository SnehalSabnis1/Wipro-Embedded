#encrypted
list1=[]
list2=[]
s="message"
for idx,char in enumerate(s):
    if idx % 2 ==0:
        list1.append(idx)
    else:
        list2.append(idx)
print(list1)
print(list2)
 
#decrypted
list1=[]
list2=[]
s="message"
for idx,char in enumerate(s):
    if idx % 2 ==0:
        print(idx,char)
    else:
        print(idx,char)
