a,b,n=map(int,input().split())
for _ in range(n):
    l,t,m=map(int,input().split())
    lo=l
    hi=100000000
    while lo<hi:
        mid=(lo+hi)//2
        count=(mid-l)+1
        first=a+(l-1)*b
        last=a+(mid-1)*b
        if last<=t and (count*(first+last))//2<=m*t:
            lo=mid+1
        else:
            hi=mid
    if mid!=lo:
        print(mid)
    else:
        count=(mid-1-l)+1
        first=a+(l-1)*b
        last=a+(mid-1-1)*b
        if last<=t and (count*(first+last))//2<=m*t and mid-1>=l:
            print(mid-1)
        else:
            print(-1)