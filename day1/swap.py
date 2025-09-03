a=int(input("enter value of a :"))
b=int(input("enter value of b :"))
a,b=b,a
'''
or
temp=a
a=b
b=temp
'''
print('after swapping \na value : ',a)
print('b value : ',b)