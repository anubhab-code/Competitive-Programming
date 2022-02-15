for _ in range(int(input())):
    n,s = map(int,input().split())
    l = list(map(int, input().split()))
    ans = 0
    flag = 1
    for i in range(n):
        s-=l[i]
        if l[ans]<l[i]:
            ans = i
        if s<0:
            break
    if s>=0:
        flag = 0
    if flag:
        print(ans+1)
    else:
        print(0)