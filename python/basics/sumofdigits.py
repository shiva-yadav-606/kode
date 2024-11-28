a=eval(input('integers:'))
for num in (a):
    s=0
    temp=num
    while num>0:
        x=num%10
        s=s+x
        num=num//10
    print('sum of digits of',temp,'=',s)
