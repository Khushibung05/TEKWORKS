n=int(input("enter no. of consumers:"))
for _ in range(n):
    snum=int(input("enter consumer number :"))
    sname=input("enter name of consumer :")
    pmr,lmr=map(float,input("enter current month reaDING and last month reading : ").split())
    tu=pmr-lmr
    if tu>=1 and tu<=50:
        cbill=tu*3.80
        print('total number of units: ',tu)
        print('current bill of cunsumer ',_+1,': ',cbill)
    elif tu>=51 and tu<=100:
        cbill=50*3.80 +(tu-50)*4.20
        print('total number of units: ',tu)
        print('current bill of cunsumer ',_+1,': ',cbill)
    elif tu>100 and tu<=200:
        cbill=50*3.80+50*4.20+(tu-100)*5.10
        print('total number of units: ',tu)
        print('current bill of cunsumer ',_+1,': ',cbill)
    elif tu>200 and tu<=300:
        cbill=50*3.80+50*4.20+100*5.10+(tu-200)*6.30
        print('total number of units: ',tu)
        print('current bill of cunsumer ',_+1,': ',cbill)
    elif tu>300:
        cbill=50*3.80+50*4.20+100*5.10+100*6.30+(tu-300)*7.50
        print('total number of units: ',tu)
        print('current bill of cunsumer ',_+1,': ',cbill)
    else:
        print("invalid")
