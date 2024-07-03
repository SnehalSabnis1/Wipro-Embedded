import re
s1 = """the name of the employee is Bob Smith and his designation is developer 
and we have one more employee named Pat Smith and his designation is devops"""

p = re.compile(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)')

val = p.search(s1)

for val in p.finditer(s1):
    print(val.group(1))
