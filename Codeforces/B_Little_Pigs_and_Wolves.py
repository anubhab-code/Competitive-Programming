n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append([i for i in input()])
ans=0
for i in range(n):
    for j in range(m):
        if l[i][j]=="W":
            if i!=0 and l[i-1][j]=="P":
                ans+=1
                l[i-1][j]="."
            elif j!=0 and l[i][j-1]=="P":
                ans+=1
                l[i][j-1]="."
            elif i!=n-1 and l[i+1][j]=="P":
                ans+=1
                l[i+1][j]="."
            elif j!=m-1 and l[i][j+1]=="P":
                ans+=1
                l[i][j+1]="."
print(ans)