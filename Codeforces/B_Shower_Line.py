l=[]
for a in range(5):
    l.append(list(map(int,input().split())))
ans=0
for i in range(0,5):
    for j in range(0, 5):
        for k in range(0, 5):
            for n in range(0, 5):
                for m in range(0, 5):
                    if i==j or i==k or i==n or i==m or j==k or j==n or j==m or k==n or k==m or m==n:
                        continue
                    else:
                        test=l[i][j]+l[j][i]+l[j][k]+l[k][j]+2*(l[k][n]+l[n][k]+l[n][m]+l[m][n])
                        ans=max(ans,test)
print(ans)