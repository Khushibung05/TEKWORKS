def nsum(n):
    sum=0
    for i in range(1,n+1):
        print(i,end="+" if i<n else "=")
        sum=sum+i
    return sum

n=int(input("Enter a number:"))
print(f"{nsum(n)}")