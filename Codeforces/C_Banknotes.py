for _ in range(int(input())):
    n,k=map(int,input().split())
    k+=1
    ans=0
    arr=list(map(int,input().split()))
    for i in range(n-1):
        if k>0:
            x=10**(arr[i+1]-arr[i])-1
            val=min(x,k)
            ans+=(10**(arr[i]))*val
            k-=val
    ans+=k*(10**(arr[n-1]))
    print(ans)