#run this code on local machine

fh = open('demo_2.jpg','rb')
nf = open('image_1.jpg','wb')
content = fh.read()
nf.write(content)
fh.close()
nf.close()