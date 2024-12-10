n=int(input('integer='))
for i in range(0,n):
    print((n-i)*' ',end=' ')
    for j in range (0,i+1):
        if j==0:
            k=1
        else:
            k=k*(i-j+1)//j
        print(k,end=' ')
    print()
