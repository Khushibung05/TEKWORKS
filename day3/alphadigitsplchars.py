s=input("enter any string:")
def charCheck(s):
    ac=0
    dc=0
    sc=0
    for c in s:
        if c.isalnum():
            if c.isalpha():
                ac+=1
            elif c.isdigit():
                dc+=1
        else:
            sc+=1
    return ac,dc,sc
ac,dc,sc=charCheck(s)
print(f"alphabets={ac}\ndigits={dc}\nspecial characters={sc}")