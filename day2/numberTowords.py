n=int(input("enter a number:"))
ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
'''
words=[]
while n>0:
    r=n%10
    words.append(ones[r])
    n=n//10
for i in range(len(words),0,-1):
    print(words[i-1],end=" ")
'''
for i in str(n):
    print(ones[int(i)],end=" ")