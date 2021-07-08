t=[]
w=[]
n  = int(input())
ans=0
for i in range(n):
    v=list(map(int,input().split()))
    if v[0] == 0:
        ans+=v[1]
    elif v[0] < 0:
        w.append(v)
    else:
        t.append(v)

t=sorted(t)[::-1]
w=sorted(w)

if  len(w) > len(t):
    o=1
else:
    o=0
while True:
    if o==0:
        if len(t)>0:
            ans+=t[-1][1]
            t.pop()
            o=1
        else:
            break
    elif o==1:
        if len(w)>0:
            ans+=w[-1][1]
            w.pop()
            o=0
        else:
            break
print(ans)