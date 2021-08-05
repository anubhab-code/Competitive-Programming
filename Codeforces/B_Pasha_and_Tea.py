def good(mid,w,girls,boys):
    for i in range(len(girls)):
        if girls[i]<mid:
            return False
    for i in range(len(boys)):
        if boys[i]<2*mid:
            return False
    return True
n,w=map(int,input().split())
a=sorted(list(map(int,input().split())))
girls=[]
boys=[]
for i in range(n):
    girls.append(a[i])
for i in range(n,len(a)):
    boys.append(a[i])
l=0
r=w
ans=0
for i in range(65):
    mid=(l+r)/2
    if good(mid,w,girls,boys)==True:
        l=mid
        ans=mid
    else:
        r=mid
fans=0
for i in range(0,len(girls)):
    fans+=ans
for i in range(0,len(boys)):
    fans+=(ans*2)
print(min(fans,w))