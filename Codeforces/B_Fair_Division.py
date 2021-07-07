for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o=l.count(1)
    t=l.count(2)
    if o%2==0 and (t%2==0 or o>=2):
        print("YES")
    else:
        print("NO")