def delete(ls,pos):
    #ls.pop(pos)
    #return ls
    new_ls = []
    for i in range(len(ls)):
        if i != pos:
            new_ls.append(ls[i])
    return new_ls
ls=list(input("enter list elements:").split(" "))
pos=int(input("enter the position to be deleted:"))
lsr=delete(ls,pos)
print("list after deletion:",lsr)