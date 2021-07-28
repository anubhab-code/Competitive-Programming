x,y,m = map(int,input().split())
x,y = min(x,y),max(x,y)
if y>=m:
    print(0)
elif y<=0:
    print(-1)
else:
    ans = 0
    while y<m:
        q = (2*y-x)//y
        ans += q
        x,y = y,x+q*y
    print(ans)