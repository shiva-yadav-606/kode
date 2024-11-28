x=input('enter any integer:')
y=len(x)
s=0
i=0
while i<=(y-1) and i>=0:
    s=s+(int(x[i])**y)
    i=i+1
if s==int(x):
    print('given is an ARMSTRONG NUMBER')
else:
    print('not an ARMSTRONG NUMBER')

