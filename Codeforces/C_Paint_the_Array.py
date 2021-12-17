from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    r1 = 0
    r2 = 0
    for i in range(n):
        if i%2:
            r1 = gcd(r1,l[i])
        else:
            r2 = gcd(r2,l[i])
    if r1==r2 :
        print(0)
    else:
        ans = max(r1,r2)
        flag = 1
        p = min(1,l[0]%ans)
        for i in range(1,n):
            kk = min(1,l[i]%ans)
            if kk!=p:
                pass
            else:
                flag = 0
                break
            p = kk
        if not flag:
            ans = min(r1,r2)
            flag = 1
            p = min(1,l[0]%ans)
            for i in range(1,n):
                kk = min(1,l[i]%ans)
                if kk!=p:
                    pass
                else:
                    print(0)
                    flag = 0
                    break
                p = kk
            if flag:
                print(ans)
        else:
            print(ans)