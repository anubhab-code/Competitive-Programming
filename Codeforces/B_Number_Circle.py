n = int(input())
l = list(map(int,input().split()))
l = sorted(l)[::-1]
if l[0]>=l[1]+l[2]:
    print("NO")
else:
    print("YES")
    l[0],l[1]=l[1],l[0]
    print(*l)