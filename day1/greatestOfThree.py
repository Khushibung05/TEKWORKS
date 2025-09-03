a,b,c=map(int,input("enter a,b,c = ").split())
if a>b:
    if a>c:
        print(f"{a} is the greatest")
    else:
        print(f"{c} is the greatest")
else:
    if b>c:
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")

