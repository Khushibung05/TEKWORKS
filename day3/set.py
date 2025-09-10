def setInsert(s,n):
    for _ in range(n):
       ele=input("Enter the element to be inserted:")
       s.add(ele)
    return s
s=set()
n=int(input("Enter the number of elements to be inserted"))
setInsert(s,n)
print("set:",s)