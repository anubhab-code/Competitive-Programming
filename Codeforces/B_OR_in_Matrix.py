n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
    
p=[[1 for i in range(m)]for j in range(n)]
#print(p)
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            p[i]=[0 for x in range(m)]
            for k in range(n):
                p[k][j]=0

q=[[0 for i in range(m)]for j in range(n)]
#print(q)
for i in range(n):
    for j in range(m):
        #if l[i][j]==1:
        if p[i][j]==1:
            q[i]=[1 for y in range(m)]
            for k in range(n):
                q[k][j]=1
if q==l:
    print("YES")
    for i in p:
        print(*i)
else:
    print("NO")