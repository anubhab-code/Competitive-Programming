n = int(input())
l = list(map(int,input().split()))
m = int(input())
for i in range(m):
    w,h = map(int,input().split())
    ans = max(l[0],l[w-1])
    print(ans)
    l[0]=ans+h