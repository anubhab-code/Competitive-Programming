a,b = map(int, input().split())
if b<=a:
    print(a-b)
else:
    ans = 0
    while b>a:
        if b%2!=0:
            b+=1
        else:
            b//=2
        ans+=1
    print(ans+a-b)