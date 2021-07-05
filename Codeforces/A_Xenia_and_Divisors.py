n = int(input())
l = list(map(int, input().split()))
if 5 in l:
    print(-1)
elif 7 in l:
    print(-1)
else:
    o = l.count(1)
    t = l.count(2)
    th = l.count(3)
    f = l.count(4)
    s = l.count(6)

    if o==(f+s) and o==(t+th) and t>=f and s>=th:
        p  = []
        for i in range(o):
            p.append(1)
            if t>0:
                p.append(2)
                t = t -1
            elif th>0:
                p.append(3)
                th = th -1
            if f>0:
                p.append(4)
                f = f-1
            elif s>0:
                p.append(6)
                s = s -1
            print(*p)
            p.clear()
    else:
        print(-1)