for _ in range(int(input())):
    n=int(input())
    r1=list(map(int,input()))
    r2=list(map(int,input()))
    ans=0
    for i in range(n):
        check=0
        if r2[i]==1:
            if r1[i]==0:
                ans+=1
            else:
                if i!=0:
                    if r1[i-1]==1:
                        r1[i-1]=0
                        check=1
                        ans+=1
                if i!=n-1 and not check:
                    if r1[i+1]==1:
                        r1[i+1]=0
                        check=1
                        ans+=1
    print(ans)