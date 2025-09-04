def prime(n):
    if n>1:
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                return False
    return True
num=int(input("enter a number :"))
if prime(num) == True:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")