str=input("enter a string:")
wc=0
for i in str:
    if i==" " or i=="\n":
        wc+=1
print("no. of words=",wc+1)
