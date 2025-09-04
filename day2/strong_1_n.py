n=int(input("enter a number:"))
def fact(r):
    if r==0 or r==1:
        return 1
    else:
        return r*fact(r-1)
print("strong numbers:")
for i in range(1,n+1):
    s=0
    t=i
    while i>0:
        r=i%10
        s=s+fact(r)
        i=i//10
    if t==s:
        print(f"{t}",end=" ")