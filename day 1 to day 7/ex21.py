#fh = open('readme.txt','r')

#print(fh.name)
#print(fh.mode)
#print(fh.closed)

#fh.close()

#fh = open('readme.txt','r')
#print(fh.read())
#fh.close()

#fh = open('readme.txt','r')
#print(fh.readline())
#print(fh.readline())
#fh.close()

#fh =  open('readme.txt','r')
#for num,line in enumerate(fh.readlines(),1):
 #   if num >=3 and num <=5:
  #      print(line)
#fh.close

fh = open('readme.txt','a')
fh.write("Python is portable\n")
fh.write("Python is extendable\n")
fh.close()
