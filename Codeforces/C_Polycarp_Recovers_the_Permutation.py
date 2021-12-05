for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = max(l)
    ans = []
    for i in l:
        if i!=m:
            ans = [i]+ans
    if l[0]==m:
        print(m,*ans)
    elif l[-1]==m:
        print(m,*ans)
    else:
        print(-1)
    