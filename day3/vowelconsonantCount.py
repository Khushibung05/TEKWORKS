vowels="aeiouAEIOU"
str=input("enter a string:")
vc=0
cc=0
for i in str:
    if i in vowels:
        vc+=1
    else:
        cc+=1
print("no. of vowels=",vc)
print("no. of consonants=",cc)