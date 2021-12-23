from collections import defaultdict
for _ in range(int(input())):
    n,m=map(int,input().split())
    s=set([i for i in range(1,n+1)])
    temp=[]
    for _ in range(m):
        a,b,c=map(int,input().split())
        if b in s:
            s.remove(b)
        temp.append((a,b,c))
    sto=-1
    for i in s:
        sto=i
        break
    for j in range(1,n+1):
        if sto==j:
            continue
        print(sto,j)