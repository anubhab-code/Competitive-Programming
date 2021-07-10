r,c=map(int,input().split())
l=[[0]*c for i in range(r)]
if r==1 and c==1:
    print(0)
    exit()
if r==1 or c==1:
    for i in range(2,r+c+1):
        print(i,end=" ")
    exit()    
for i in range(r):
    ans=(r+1)*(i+1)
    for j in range(c):
        l[i][j]=ans
        ans+=i+1
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()