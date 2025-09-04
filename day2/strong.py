n=int(input("enter a number:"))
def fact(r):
    if r==0 or r==1:
        return 1
    else:
        return r*fact(r-1)
s=0
t=n
while n>0:
    r=n%10
    s=s+fact(r)
    n=n//10
if t==s:
    print(f"{t} is a strong number")
else:
    print(f"{t} is not a strong number")