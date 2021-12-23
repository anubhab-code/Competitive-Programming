for _ in range(int(input())):
    l,r=map(int,input().split())
    b=r
    a=r//2+1
    if a<l:
        a=l
    if a>r:
        a=r
    print(b%a)