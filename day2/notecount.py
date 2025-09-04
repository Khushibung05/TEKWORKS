notes=[2000,500,200,100,50,20,10]
amount=int(input("enter amount:"))
ac={}
for note in notes:
    count=amount//note
    if count>0:
        ac[note]=count
        amount=amount%note
print(ac)