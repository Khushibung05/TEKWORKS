def stringLength(s):
    c=0
    for i in s:
        c+=1
    return c
def stringCompare(s1,s2):
    if s1==s2:
        return True
    else:
        return False
def strConcat(s1,s2):
    return s1+s2
s1=input("enter a string:")
s2=input("enter a string:")
print(f"length of sting is:{stringLength(s1)}")
print(f"both string equal? {stringCompare(s1,s2)}")
print(f"s1+s2={strConcat(s1,s2)}")