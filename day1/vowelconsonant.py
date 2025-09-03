vowels='aeiouAEIOU'
a=input("enter a character :")
if a.isalpha():
    if a in vowels:
        print(f"{a} is vowel")
    else:
        print(f"{a} is a consonant")
else:
    print("enter an alphabet")