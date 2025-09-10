ls=list(input("enter the list elements:").split(" "))
for i in range(len(ls)):
    if int(ls[i])>0:
        print(ls[i],end=" ")