x=input("enter any alphabet:")
y=ord(x)
if 65<=y<=90:
    print(chr(y+32))
else:
    print(chr(y-32))
