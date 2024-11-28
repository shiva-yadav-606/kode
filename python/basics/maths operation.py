a=float(input('enter first number='))
b=float(input('enter second number='))
op=input('enter any mathematical operator=')
add='+'
sub='-'
mod='%'
div='/'
floor='//'
multiply='*'
power='**'
if op==add:
    print(a+b)
elif op==sub:
    print(a-b)
elif op==mod:
    print(a%b)
elif op==floor:
    print(a//b)
elif op==multiply:
    print(a*b)
elif op==power:
    print(a**b)
elif op==div:
    print(a/b)
