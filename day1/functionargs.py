#with args,without return
#add
'''
def add(a,b):
    c=a+b
    print(f"a+b={c}")
x,y=map(int,input("enter x and y values:").split())
add(x,y)

#km to miles
def kmTomiles(km):
    miles=km*0.621371
    print(f"miles = {miles}")
km=int(input("enter kilometers:"))
kmTomiles(km)
'''
#convert days to year and months
def convertToym(d):
    year=int(d/365)
    months=int(d/30)
    print(f"{d} days={year} years,{months} months")
days=int(input("enter no. of days"))
convertToym(days)