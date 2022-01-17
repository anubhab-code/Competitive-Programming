n = int(input())
l = list(map(int,input().split()))
c = {}
for i in l:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
ans,anss=0,0
x = max(l)
for i in set(l):
    for j in range(1,32):
        a = 2**j - i
        if a>x:
            break
        if a in c:
            if i==a:
                anss += c[a]*(c[a]-1)//2
            else:
                ans += c[a]*c[i]
print(ans//2+anss)