def listInsert(l,n):
    for _ in range(n):
       ele=input("Enter the element to be inserted:")
       l.append(ele)
    return l
l=[]
n=int(input("Enter the number of elements to be inserted"))
listInsert(l,n)
print("list:",l)