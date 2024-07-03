#while True:
   # try:
     #   x=int(input("Enter a number"))
    #    print(x)
   #     break
  #  except:
 #      print("Not a valid number")

#x=int(input("Enter a number"))  
#print(x)
#print("Continuing the script...")

#try:
 #   x=int(input("Enter a number"))
 #   print(x)        
#except:
 #      print("some error")
#print("Continuing the script...")

import sys
try:
    x=int(input("Enter a number"))
    print(x)        
except ValueError:
       print("some error",sys.exc_info())
print("Continuing the script...")
