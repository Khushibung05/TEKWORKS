n=int(input("enter no. of students:"))
for _ in range(n):
    snum=int(input("enter student number :"))
    sname=input("enter name of student :")
    chem,phy,math=map(float,input("enter marks for chemistry,physics,maths :").split())
    total=chem+phy+math
    avg=total/3
    print('total of student ',_+1,':',total)
    print('average of student ',_+1,':',round(avg,2))
    if chem>=40 and phy>=40 and math>=40:
        print("PASS")
        if avg<=50:
            print("grade : C")
        elif avg>=51 and avg<=70:
            print("garde : B")
        elif avg>=71 and avg<=80:
            print("garde : A")
        elif avg>=81:
            print("DISTINCTION")
    else:
        print("FAIL")