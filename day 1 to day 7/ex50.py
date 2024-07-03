import re
s1 = """the name of the employee is Bob Smith and his email is bobsmith@example.com 
and we have one more employee named Pat Smith and his email is patsmith@example.com"""

p = re.compile(r'(\b[a-z]+@[a-z]+\.[a-z]+\b)')

val = p.search(s1)

for val in p.finditer(s1):
    print(val.group(1))