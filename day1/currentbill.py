n=int(input("enter no. of consumers:"))
for _ in range(n):
    snum=int(input("enter consumer number :"))
    sname=input("enter name of consumer :")
    pmr,lmr=map(float,input("enter current month reaDING and last month reading : ").split())
    tu=pmr-lmr
    cbill=tu*3.80
    print('total number of units: ',tu)
    print('current bill of cunsumer ',_+1,': ',cbill)