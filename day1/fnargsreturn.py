def add(a,b):
    c=a+b
    return c
x,y=map(int,input("enter x and y values:").split())
print(f"a+b={add(x,y)}")