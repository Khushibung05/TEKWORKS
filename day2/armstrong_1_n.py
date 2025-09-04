n=int(input("enter a number:"))
print("armstrong numbers:")
for i in range(1,n+1):
    s=0
    t=i
    while i>0:
        r=i%10
        s=s+r**3
        i=i//10
    if t==s:
        print(f"{t}",end=" ")
