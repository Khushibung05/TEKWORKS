def topStudent(l):
    max=0
    for i in range(len(l)):
        if l[i][2]>max:
            max=l[i][2]
            name=l[i][0]
    return name
def stuGT75(l):
    for i in range(len(l)):
        if l[i][2]>75:
            print(l[i][0],end=" ")
l=[]
n=5
for i in range(n):
    print("enter name of student ",i+1)
    name=input()
    print("enter rollno of student ",i+1)
    rollno=input()
    print("enter marks of student ",i+1)
    marks=float(input())
    l.append(tuple([name,rollno,marks]))
print(l)
print("student with highest marks is:",topStudent(l))
print("students scored > 75 are:")
stuGT75(l)