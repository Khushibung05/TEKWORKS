def prime(l):
    for n in l:
        if n>1:
            for i in range(2,int(n**0.5+1)):
                if n%i==0:
                    return False
        return True
n=int(input("Enter a number:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(f"prime factors of {n} are:")
