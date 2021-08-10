a=[]
for i in range(int(input())):
    x,y=map(int,input().split())
    a.append([x,y])
a=sorted(a)
ans=0
rg=a[0][1]
for i in range(len(a)):
    if a[i][1]>rg:
        rg=a[i][1]
    else:
        ans+=1
print(ans-1)