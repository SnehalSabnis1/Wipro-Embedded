import re
s1 = "in jinja template variables are given inside {{myname}} like this"
val = re.search(r'.*\{\{(.*)\}\}',s1)

if val :
    print(val.group(1))
    
else :
    print("not matched")