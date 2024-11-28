a=int(input('enter lower limit='))
b=int(input('enter upper limit='))
for num in range(a,b+1):
    temp=num
    y=len(str(num))
    s=0
    while num>0:
        r=num%10
        s=s+r**y
        num=num//10
    if s==temp:
        print(temp)
    else:
        pass
        
