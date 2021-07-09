n=int(input())
x={}
y={}
z={}
ans=0
for i in range(n):
    q,w=map(int,input().split())
    if q in x:
        x[q]+=1
    else:
        x[q]=1
    if w in y:
        y[w]+=1
    else:
        y[w]=1
    p=str([q,w])
    if p in z:
        z[p]+=1
    else:
        z[p]=1
for i in x:
    o=x[i]
    ans+=o*(o-1)//2
for i in y:
    o=y[i]
    ans+=o*(o-1)//2
for i in z:
    o=z[i]
    ans-=o*(o-1)//2
print(ans)