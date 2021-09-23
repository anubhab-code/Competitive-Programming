for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l
    a=sorted(a)
    ans=0
    while 1:
        if a==l:
            break
        if ans%2==0:
            for i in range(0,n-1,2):
                if l[i]>l[i+1]:
                    l[i],l[i+1]=l[i+1],l[i]
            ans+=1
        else:
            for i in range(1,n,2):
                if l[i]>l[i+1]:
                    l[i],l[i+1]=l[i+1],l[i]
            ans+=1
    print(ans)