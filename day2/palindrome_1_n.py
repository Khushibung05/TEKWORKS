n=int(input("enter a number:"))
for i in range(1,n+1):
    if str(i)==str(i)[::-1] and i>9: 
        print(f"{i}",end=" ")