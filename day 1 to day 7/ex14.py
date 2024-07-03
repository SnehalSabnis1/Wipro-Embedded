x=20
def f():
    y=10
    print("y inside function:",y)
f()
print("global scope:",x)
#print("local scope:",y)

x=20
def f():
    z=5
    print("x inside function:",x)
    print("z is inside function:",z)
f()
print("x outside function:",x)

x=20
def f():
    x=10
    z=5
    print("x inside function:",x)
    print("z is inside function:",z)
f()
print("x outside function:",x)

def f():
    z=5
    print("z is inside function:",z)
    global x
    x=10
    print("x inside function:",x)
f()
print("x outside function:",x)

##
def perfect(num):
    str_num = str(num)


    for digit in str_num:
        int_digit = int(digit)


        if int_digit == 0 or num % int_digit != 0:
            return False
    return True
   
for num in range(141, 152):
    if perfect(num):
        print(f"{num} is perfect.")
    else:
        print(f"{num} is not perfect.")
