for _ in range(int(input())):
    n,c0,c1,h=map(int,input().split())
    s=input()
    ans=0
    if c0==c1:
        print(len(s)*c0)
    else:
        for i in s:
            if i=='0':
                ans+=+min(c0,h+c1)
            elif i=='1':
                ans+=min(c1,c0+h)
        print(ans)