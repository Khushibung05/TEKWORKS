def frequency(str):
    freq={}
    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
str=input("enter a string:")
d=frequency(str)
print("frequency of characters:",d)
