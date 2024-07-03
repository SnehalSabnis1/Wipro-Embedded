#Spring Functions

s1="helloworld"
s2=s1.upper()
print(s2)

print(s1.find('w'))
print(s1.index('o'))
print(s1.count('l'))

#s1[2]='m'
#print(s1)

list1=['bob@gmail.com','alice@gmail.com','tom@example.com']
for element in list1:
    if element.endswith('gmail.com'):
        print(element)

s1="gdty56io"
for char in s1:
    if char.isdigit():
        print(char)

s1="cat sat on the mat"
