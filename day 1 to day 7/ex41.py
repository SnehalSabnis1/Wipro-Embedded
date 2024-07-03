import re
s1 = input("Enter a string\n")
val = re.search(r"https?://www.mydomain.com",s1)

if val :
    print("matched")
else :
    print("not matched")