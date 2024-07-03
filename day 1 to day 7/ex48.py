import re
s1 = "the name of the employee is Bob Smith and his designation is developer"

p = re.compile(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)')

val = p.search(s1)

if val:
    print(val.group(1))
else :
    print("not matched")