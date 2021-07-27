n = int(input())
a = list(map(int, input().split()))
mx,mn = 1000,1000
ans = [[" "] * 2020 for i in range(2020)]
x,y = 1000,0
for i in range(n):
    if i%2==0:
        for j in range(a[i]):
            ans[x][y] = "/"
            x-=1
            y+=1
        x+=1
    else:
        for j in range(a[i]):
            ans[x][y] = "\\"
            x+=1
            y+=1
        x-=1
    mx = max(mx,x)
    mn = min(mn,x)
for i in range(mn,mx+1):
    print("".join(ans[i][:y]))