def leap(year):
    if year%4==0 or year%400==0 and year%100!=0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
y=int(input("enter an year:"))
leap(y)