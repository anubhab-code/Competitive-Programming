for _ in range(int(input())):
    n=int(input())
    l=list(input())
    start=-1
    end=-1
    t=0
    for i in range(n):
        if l[i]=='*' and start==-1:
            start=i
        elif l[i]=='*':
            end=i
        if l[i]=='*':
            t+=1
    if start==-1 or end==-1:
        print(0)
    elif end-start+1 == t:
        print(0)
    else:
        ans=0
        prev=0
        for i in range(n):
            if l[i]=='*':
                prev += 1
            else:
                ans += min(prev,t-prev)
        print(ans)