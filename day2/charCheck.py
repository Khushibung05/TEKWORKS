c=input("enter any character:")
if c.isalnum():
    if c.isalpha():
        print(f"{c} is an alphabet")
    elif c.isdigit():
        print(f"{c} is a digit")
else:
    print(f"{c} is a special character")