n=int(input("enter a number :"))
'''
s=str(n)
first=int(s[0])
last=int(s[-1])
print(f"first digit is {first} and last digit is last {last}")
print(f"sum of first and last digit is {first+last}")
'''
first=0
last=0
while n>0:
    r=n%10
    if last==0:
        last=r
    first=r
    n=n//10
print(f"first digit is {first} and last digit is last {last}")
print(f"sum of first and last digit is {first+last}")