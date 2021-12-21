a,b,c,d=map(int,input().split())
if a>c:
    a,c=c,a
if b>d:
    b,d=d,b
z=[tuple(map(int,input().split())) for _ in " "*int(input())]
ans=0
for i in range(a,c+1):
    for x,y,r in z:
        if (i-x)**2+(y-b)**2<=r**2:
            break
    else:
        ans+=1
for i in range(b+1,d):
    for x,y,r in z:
        if (c-x)**2+(i-y)**2<=r**2:
            break
    else:
        ans+=1
for i in range(a,c+1):
    for x,y,r in z:
        if (i-x)**2+(y-d)**2<=r**2:
            break
    else:
        ans+=1
for i in range(b+1,d):
    for x,y,r in z:
        if (a-x)**2+(i-y)**2<=r**2:
            break
    else:
        ans+=1
print(ans)