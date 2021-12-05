for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    ans=l[0]
    temp=ans
    for i in range(1,n):
        if ans<(l[i]-temp):
            ans=l[i]-temp
        temp+=l[i]-temp
    print(ans)