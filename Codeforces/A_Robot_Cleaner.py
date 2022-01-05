for _ in range(int(input())):
    n,m,rb,cb,rd,cd=map(int,input().split())
    ans=0
    s1,s2=1,1
    while rb!=rd and cb!=cd:
        if cb==m:
            s2*=-1
        if rb==n:
            s1*=-1
        cb+=s2
        rb+=s1
        ans+=1
    print(ans)