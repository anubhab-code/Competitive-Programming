n,r,avg = map(int,input().split())
f=[]
u=0
for j in range(n):
    a,b = map(int,input().split())
    u+=a
    f.append([b,a])
f=sorted(f)
if u/n >= avg:
    print(0)
else:
    req = avg*n - u
    ans = 0
    for j in range(n):
        if f[j][1]<r:
            got = r-f[j][1]
            g=min(got,req)
            ans+=g*f[j][0]
            req-=g
            if req==0:
                print(ans)
                break