for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(input())
    s1=s[:k]
    s1.reverse()
    if k==0:
        print("YES")
    elif s1==s[n-k:] and k<=(n-1)//2:
        print("YES")
    else:
        print("NO")