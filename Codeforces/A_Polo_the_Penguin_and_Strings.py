n,k=map(int,input().split())
if k>n:
    print(-1)
elif n==1 and k==1:
    print("a")
elif k==1:
    print(-1)
else:
    ans=""
    k=k-2
    n=n-k
    z=99
    if n%2==0:
        ans+="ab"*(n//2)
        while(k>0):
            ans+=chr(z)
            z+=1
            k-=1
    else:
        x=99
        ans+="ab"*(n//2)
        ans+="a"
        while(k>0):
            ans += chr(x)
            x+= 1
            k-=1
    print(ans)