import sys
try:
    f = open('myfile.txt','r')
    s = f.readline()
    s = s.strip()
    nums = s.split()
    i = int(nums[0])
    print(i)   
except IOError as e:
      print("I/O erroe ({0}) ")     
except ValueError:
       print("some error",sys.exc_info())
print("Continuing the script...")
