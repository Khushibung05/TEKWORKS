def prime(n):
    for j in range(1,n+1):
        if j>1:
            for i in range(2,int(j**0.5+1)):
                if j%i==0:
                    return False
            print(j,end=" ")
    
num=int(input("enter a number :"))
prime(num)