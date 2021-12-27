for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    check=min(l)
    ans=0
    c=0
    while ans!=n//2:
        if l[c]!=check:
            print(l[c],check)
            c+=1
            ans+=1
        else:
            c+=1