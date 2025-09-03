def divFiveEleven(num):
    if num%5==0 and num%11==0:
        return True
    return False
num=int(input("enter a num:"))
if(divFiveEleven(num)==True):
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")
