def negative(num):
    if num<0:
        return True
    return False
num=int(input("enter a num:"))
if(negative(num)==True):
    print(f"{num} is nrgative")
else:
    print(f"{num} is positive")