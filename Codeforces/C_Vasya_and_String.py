n,k = list(map(int,input().split()))
st = input()
ans = 1
for i in ['a','b']:
    l=0
    r=0
    if st[l]!=i:
        s=1
    else:
        s=0
    while l<n:
        if s<=k:
            r+=1
            if r==n:
                break
            if st[r]!=i:
                s+=1
        else:
            l+=1
            if st[l-1]!=i:
                s-=1
        if s<=k:
            ans=max(r-l+1,ans)
print(ans)