import re
s1 = "this is my input which has $ some characters between doller $ and need to be extracted"
val = re.search(r'.*\$(.*)\$.*',s1)

if val :
    print(val.group(1))

else :
    print("not matched")