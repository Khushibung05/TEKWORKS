def eveoddc(ls):
    ec=0
    oc=0
    for i in range(len(ls)):
        if int(ls[i])%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc
ls=list(input("enter list elements:").split(" "))
ec,oc=eveoddc(ls)
print("even count=",ec)
print("odd count=",oc)