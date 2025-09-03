def add():
    a,b=map(int,input("enter x and y values:").split())
    c=a+b
    return c

print(f"a+b={add()}")