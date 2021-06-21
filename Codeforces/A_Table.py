n,m = map(int,input().split())
l=[]
for i in range(n):
    l.append([])
    l[i] = list(map(int,input().split()))
check=0
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            if (i==0 or i==n-1) or (j==0 or j==m-1):
                check=1
if check==0:
    print(4)
else:
    print(2)