for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)
    for i in range(n):
        for j in range(m):
            if i%2==1:
                if j%2==1:
                    if l[i][j]%2==0:
                        l[i][j]+=1
                else:
                    if l[i][j]%2==1:
                        l[i][j]+=1
            else:
                if j%2==0:
                    if l[i][j]%2==0:
                        l[i][j]+=1
                else:
                    if l[i][j]%2==1:
                        l[i][j]+=1
    for i in l:
        print(*i)