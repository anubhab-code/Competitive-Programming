n,m=map(int,input().split())
l=[]
for i in range(n):
    new=list(map(int,input().split()))
    l.append(new)
ans=[]
for i in range(n):
    ans.append([0]*m)
for i in range(n):
    for j in range(m):
        if (i+j)%2==1:
            ans[i][j]=720720 #lcm of first 16 numbers
        else:
            ans[i][j]=720720+(l[i][j])**4
for k in range(n):
    print(*ans[k])