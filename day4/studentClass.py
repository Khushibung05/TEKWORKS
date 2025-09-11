class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")
n=int(input("Enter number of students:"))
'''s1=Student("Alice","101",400)
s2=Student("Bob","102",350)
s1.display()
s2.display()
'''
students=[]
for _ in range(n):
    name=input("enter name :")
    roll_no=input("enter roll no:")
    marks=float(input("enter marks:"))
    students.append(Student(name,roll_no,marks))
for student in students:
    student.display()