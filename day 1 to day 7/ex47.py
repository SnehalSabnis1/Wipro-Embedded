import re
s1 = "hi hello world"
val = re.search(r'\bhello\b',s1)

if val :
    print("matched")

else :
    print("not matched")
