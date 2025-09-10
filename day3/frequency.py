def frequency(l):
    freq={}
    for i in l:
        print(i)
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
ls=list(input("enter list elements:").split(" "))
d=frequency(ls)
print("frequency of elements:",d)