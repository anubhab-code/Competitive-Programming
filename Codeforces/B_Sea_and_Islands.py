n,k = map(int,input().split())
temp = (n*n + 1)//2
if k<=temp:
    print("YES")
    ans = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append('S')
        ans.append(x)
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0 and k:
                ans[i][j]='L'
                k-=1
    for i in range(n):
        for j in range(n):
            print(ans[i][j],end='')
        print()
else:
    print("NO")