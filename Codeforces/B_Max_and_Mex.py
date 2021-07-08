import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l=sorted(l)
    mex = l[-1]+1
    for i in range(n):
        if l[i]!=i:
            mex=i
            break
    mx = l[-1]
    if k==0 or mx-mex==1:
        print(len(set(l)))
    elif mex<mx:
        l.append(math.ceil((mex+mx)/2))
        print(len(set(l)))
    else:
        print(len(set(l))+k)