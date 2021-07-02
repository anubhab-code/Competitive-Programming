n,k=map(int,input().split())
c=0
ans=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(k-1):
        c+=1
        ans[i][j]=c
final=0
for i in range(n):
    for j in range(k-1,n):
        c+=1
        ans[i][j]=c
    final+=ans[i][k-1]
print(final)
for i in ans:
    print(*i)