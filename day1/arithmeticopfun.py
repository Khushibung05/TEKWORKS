def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modulus(a,b):
    return a%b
def exponentiatin(a,b):
    return a**b
def floord(a,b):
    return a//b
x,y=map(int,input("enter x and y values : ").split())
print(f"sum={add(x,y)} \ndifference={sub(x,y)} \nproduct={mul(x,y)} \nquotient={div(x,y)} \nremainder={modulus(x,y)} \npower={exponentiatin(x,y)} \nfloor={floord(x,y)}")