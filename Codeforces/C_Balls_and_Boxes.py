n,x=map(int,input().split())
A=list(map(int,input().split()))
x-=1
if 0 in A[:x]:
    cnt=0
    while A[x]!=0:
        cnt+=1
        A[x]-=1
        x-=1
    A[x]=cnt
elif 0 in A[x+1:]:
    cnt=0
    for i in range(x+1):
        A[i]-=1
        cnt+=1
    for i in range(n-1,-1,-1):
        if A[i]==0:
            A[i]+=cnt
            break
        A[i]-=1
        cnt+=1
else:
    m=min(A)
    idx=-1
    for i in range(x,-1,-1):
        if A[i]==m:
            idx=i
            break
    if idx==-1:
        for i in range(x+1,n):
            if A[i]==m:
                idx=i
                break
    cnt=0
    for i in range(n):
        A[i]-=m
        cnt+=m
        if (idx<=x and idx<=i<=x) or (idx>x and not (x<i<=idx)):
            A[i]-=1
            cnt+=1
    A[idx]+=cnt
print(*A)