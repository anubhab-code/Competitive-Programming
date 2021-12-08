for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    for i in range(len(l)):
        l[i]-=i+1
        if l[i]<=ans:
            continue
        else:
            ans = l[i]
    print(ans)