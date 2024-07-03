fh=open('file2.txt','w+')

fh.write('Programming in Python is fun\n')
fh.write('Python is easy to learn\n')

fh.seek(0,0)
print(fh.read())

fh.close()