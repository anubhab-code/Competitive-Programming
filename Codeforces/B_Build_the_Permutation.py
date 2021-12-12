for _ in range(int(input())):
    n,a,b=map(int,input().split())
    l,r=1,n
    ans=[]
    if a+b>n-2 or abs(a-b)>1:
        print(-1)
    else:
        if a==b:
            h,v=0,0
            ans.append(l)
            l+=1
            while h<a:
                ans.append(r)
                r-=1
                ans.append(l)
                l+=1
                h+=1
            for i in range(l,r+1):
                ans.append(i)
        elif a>b:
            h=0
            ans.append(l)
            l+=1
            while h<a-1:
                ans.append(r)
                r-=1
                ans.append(l)
                l+=1
                h+=1
            i=r
            while i>=l:
                ans.append(i)
                i-=1
        else:
            v=0
            ans.append(r)
            r-=1
            while v<b-1:
                ans.append(l)
                l+=1
                ans.append(r)
                r-=1
                v+=1
            for i in range(l,r+1):
                ans.append(i)
    print(*ans)
            
            
            
            