import re
s1 = input("Enter a string\n")
val = re.search(r'.*\.(.*)\..*',s1)

if val :
    print(val.group(1))
else :
    print("not matched")