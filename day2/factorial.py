def fact(n):
    if n==1:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
            print(n-i+1,end="*" if i<n else "=")
    return f
n=int(input("enter a number:"))
print(f"{fact(n)}!")
