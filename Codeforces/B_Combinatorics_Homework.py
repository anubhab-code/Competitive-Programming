for _ in range(int(input())):
    a,b,c,m = map(int,input().split())
    mn = 2*max(a,b,c)-(a+b+c)-1
    mx = a+b+c-3
    if m<=mx and m>=mn:
        print("YES")
    else:
        print("NO")