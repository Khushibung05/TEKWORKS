nr,de=map(int,input("enter numerator and denominator:").split(" "))
try:
    result=nr/de
    print("Result:",result)
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
    
