s={i for i in ("shiva")}
for i in s:
    print(i) # a set doesn't follow order
#to create an empty set
shiv=set()
print(type(shiv))#will return set
#but this is wrong
shiv={}
print(type(shiv))#will return dict