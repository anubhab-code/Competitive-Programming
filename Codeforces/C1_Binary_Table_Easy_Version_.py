for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(input())
    ans=[]
    for i in range(n):
        for j in range(m):
            if l[i][j]=='1':
                if i!=n-1 and  j!=m-1:
                    ans.append([i+1,j+1,i+2,j+1,i+1,j+2])
                    ans.append([i+1,j+1,i+2,j+1,i+2,j+2])
                    ans.append([i+1,j+1,i+1,j+2,i+2,j+2])
                elif i==n-1 and j!=m-1:
                    ans.append([i+1,j+1,i,j+1,i+1,j+2])
                    ans.append([i+1,j+1,i,j+1,i,j+2])
                    ans.append([i+1,j+1,i+1,j+2,i,j+2])
                elif  i!=n-1 and j==m-1:
                    ans.append([i+1,j+1,i+1,j,i+2,j+1])
                    ans.append([i+1,j+1,i+1,j,i+2,j])
                    ans.append([i+1,j+1,i+2,j+1,i+2,j])
                elif i==n-1 and j==m-1:
                    ans.append([i+1,j+1,i+1,j,i,j+1])
                    ans.append([i+1,j+1,i+1,j,i,j])
                    ans.append([i+1,j+1,i,j+1,i,j])
    print(len(ans))
    for k in ans:
        print(*k)