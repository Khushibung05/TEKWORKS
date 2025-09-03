#python output
'''
print("hello")
a=5
print('the value of',a)
print(1,2,3,4)
print(1,2,3,4,sep='*')
print(1,2,3,4,sep='#',end='$')

#python input
a=input("\nEnter a value ")
print(type(a))
c=10
b=20
#error print(a+b) : str cant conctenate with int
print('c+b=',c+b)
print('a+a',a+a)
'''
#type conversion/casting : int(),str(),float(),ord(),chr()

#key things to observe for a program : i/p , processing , o/p

#1. enter radius of a circle AND FIND IT'S area: i/p=r,area,op=area

r=float(input("enter radius of circle :"))
pi=3.14
area=pi*r**2 #pi*r*r
circumferenece=2*pi*r
print('area of circle:',area)
print(' circumferenceof circle:',circumferenece)

#area and perimeter of rectangle
l=float(input("enter length of rectangle :"))
b=float(input("enter breadth of rectangle :"))
area=l*b
perimeter=2*(l+b)
print('area of rectangle:',area)
print('perimeter of rectangle:',perimeter)

#vol of cube
s=float(input("enter side of a cube : "))
vol=s**3
print('volume of cube : ',vol)

#vol of cylinder
r=float(input("enter radius of cylinder :"))
h=float(input("enter height of cylinder :"))
pi=3.14
vol=pi*h*r**2
print('volume of cylinder :',vol)

