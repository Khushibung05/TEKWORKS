p=float(input("enter principle amount : "))
t=int(input("enter total no. of months : "))
r=float(input("enter rate of interest :"))
simpleInterest=(p*t*r)/100
amountInHand=p+simpleInterest
print('simple interest :',simpleInterest)
print('total amount in hand :',amountInHand)