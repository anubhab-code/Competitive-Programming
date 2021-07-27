a=[int(i) for i in input().split(',')]
a=list(set(a))
a.sort()
l,r=a[0],a[0]
for i in range(1,len(a)):
    if a[i]-1==a[i-1]:
        r+=1
    else:
        if l==r:
            print(l,end=',')
        else:
            print(l,'-',r,sep='',end=',')
        l,r=a[i],a[i]
if l==r:
    print(l)
else:
    print(l,'-',r,sep='')