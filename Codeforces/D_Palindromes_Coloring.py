from typing import Counter
for _ in range(int(input())):
    n,k = map(int,input().split())
    c1,c2 = 0,0
    ans = 0
    s = input()
    check = Counter(s)
    for i in s:
        c1 += check[i]//2
        check[i]%=2
        c2 += check[i]
        check[i] = 0
    t1=c1//k
    ans += t1*2
    t2 = c1%k
    c2 += t2*2
    if not c2>=k:
        pass
    else:
        ans+=1
    print(ans)