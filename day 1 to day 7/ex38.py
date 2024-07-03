import re
s1 = "the name of the employee is Bob Smith and his designation is developer"
#match
#search
val = re.search(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)',s1)

if val:
    print(val.group(1))