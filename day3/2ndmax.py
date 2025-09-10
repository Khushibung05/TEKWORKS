ls=list(input("enter the list elements:").split(" "))
max=0
for i in range(len(ls)):
    if int(ls[i])>max:
        max=int(ls[i])
        secondmax=0
        for j in range(len(ls)):
            if int(ls[j])>secondmax and int(ls[j])<max:
                secondmax=int(ls[j])
print("second max is: ",secondmax)
