#import os
#print(os.getcwd())

#print(dir(os))

#print(os.uname())

#import random
#print(random.randint(1,100))

import sys
print(sys.path)
custom_path=r'C:\\Python Programming\\Lib', 'C:\\Python312'
sys.path.append(custom_path)
import hello
print(hello.addnum(10,2))
print(hello.divnum(10,2))