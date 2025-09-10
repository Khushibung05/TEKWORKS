def frequency(l):
    freq={}
    for i in l:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
ls=list(input("enter list elements:").split(" "))
d=frequency(ls)
print("unique elements in list:",list(d.keys()))
#set()