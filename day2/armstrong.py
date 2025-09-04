#armstrong number
n=int(input("enter a number:"))
s=0
t=n
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if t==s:
    print(f"{t} is an armstrong number")
else:
    print(f"{t} is not an armstrong number")