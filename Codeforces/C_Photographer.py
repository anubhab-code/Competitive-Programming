n,d=map(int,input().split())
a,b=map(int,input().split())
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append([x*a+y*b,i+1])
l=sorted(l)
ans=[]
for j in range(len(l)):
    if d>=l[j][0]:
        ans.append(l[j][1])
        d-=l[j][0]
    else:
        break
print(len(ans))
print(*ans)