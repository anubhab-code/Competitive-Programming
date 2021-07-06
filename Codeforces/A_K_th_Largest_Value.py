n,q = map(int,input().split())
l = list(map(int,input().split()))
zero = l.count(0)
one = n-zero
for _ in range(q):
    t,x = map(int,input().split())
    if t == 1:
        if l[x-1] == 1:
            zero += 1
            one -= 1
            l[x-1] = 0
        else:
            zero -= 1
            one += 1
            l[x-1] = 1
    else:
        if x<=one:
            print(1)
        else:
            print(0)