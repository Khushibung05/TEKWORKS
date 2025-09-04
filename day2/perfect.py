n=int(input("enter a number:"))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
if sum(l)==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")