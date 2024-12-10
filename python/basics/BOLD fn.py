def case():
    n=input('enter text here:')
    for el in n:
        x=ord(el)
        if 91<=x<=122:
            print(chr(ord(el)-32),end='')
        elif 65<=x<=90:
            print(chr(ord(el)+32),end='')
        else:
                print(el,end='')
for i in range(1,6):
    case()
    print()
