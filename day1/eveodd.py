def even(num):
    if num%2==0:
        return True
    return False
num=int(input("enter a num:"))
if(even(num)==True):
    print(f"{num} is even")
else:
    print(f"{num} is odd")