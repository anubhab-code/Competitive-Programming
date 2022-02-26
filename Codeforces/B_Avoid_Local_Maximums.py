for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    i=1
    ans=0
    while i<n-1:
        if l[i]>l[i-1] and l[i]>l[i+1]:
            if i<n-2:
                l[i+1]=max(l[i],l[i+2])
            else:
                l[i+1]=l[i]
            ans+=1
            i+=1
        i+=1
    print(ans)
    print(*l)