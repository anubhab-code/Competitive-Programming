n,m = map(int, input().split())
ans = "YES"
if m>0:
    l = sorted(list(map(int, input().split())))
    if 1 in l or n in l:
        ans = "NO"
    else:
        for i in range(0,m-2):
            if l[i+1] == l[i]+1 and l[i+2] == l[i+1]+1:
                ans = "NO"
                break
print(ans)