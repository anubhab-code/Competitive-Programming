from typing import Counter
for _ in range(int(input())):    
    p = input()
    h = input()
    n = len(p)
    m = len(h)
    flag=0
    if m<n:
        print("NO")
    else:
        d = Counter(p)
        for i in range(m-n+1):
            d1 = Counter(h[i:i+n])
            if d1==d:
                flag=1
                break
        if flag:
            print("YES")
        else:
            print("NO")