for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    z=l.count(0)
    o=l.count(1)
    print((2**z)*o)
    