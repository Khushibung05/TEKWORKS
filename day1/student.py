n=int(input("enter no. of students:"))
for _ in range(n):
    snum=int(input("enter student number :"))
    sname=input("enter name of student :")
    chem,phy,math=map(float,input("enter marks for chemistry,physics,maths :").split())
    total=chem+phy+math
    avg=total/3
    print('total of student ',_+1,':',total)
    print('average of student ',_+1,':',round(avg,2))