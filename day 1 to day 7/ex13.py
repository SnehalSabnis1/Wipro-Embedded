a,b=10,20
print(a)
print(b)

#a,b,c=10,20,30,40,50,60

a,b,*c=10,20,30,40,50,60
print(a)
print(b)
print(c)

def find_max(*args):
    print(type(args))
    m=args[0]
    for v in args:
        if m<v: m=v
    return m
maxval=find_max(76,83,47,984,241,760)
print(maxval)

maxval=find_max(76,83,47,684,241,760,64,845,976)
print(maxval)

def multipleParams(**kwargs):
    print(kwargs)
multipleParams(name='alice',age=11,school='cps')  

def calculate():
    subjects = ['maths', 'physics', 'chemistry', 'biology', 'english']
    marks = {}
    for subject in subjects:
        mark = float(input(f"Enter the mark for {subject}: "))
        marks[subject] = mark
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks}")
calculate()
