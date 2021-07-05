n,m=map(int,input().split())
if (n>m+1) or (m>(n+1)*2):
    print(-1)
else:
    if m<=n:
        ans=min(n,m)*'01'
        n-=min(n,m)
        m-=min(n,m)
        ans+=n*'0'
    else:
        temp=[]
        while n>0 and m>0:
            temp.append('1')
            temp.append('0')
            n-=1
            m-=1
        if m:
            temp.append('1')
            m-=1
        for i in range(len(temp)):
            if m==0:
                break
            if temp[i]=='1':
                temp[i]='11'
                m-=1
        ans=''.join(temp)
    print(ans)