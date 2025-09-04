n=int(input("enter a number:"))
print("perfect numbers:")
for i in range(1,n+1):
    l=[]
    for j in range(1,i):
        if i%j==0:
            l.append(j)
    if sum(l)==i:
        print(f"{i}",end=" ")