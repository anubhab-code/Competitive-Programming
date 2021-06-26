n, st = map(int, input().split())
mini, maxi = [], []
for i in range(n):
    x, y = map(int, input().split())
    mini.append(x)
    maxi.append(y)
if st > sum(maxi) or st < sum(mini): 
    print("NO")
else:
    res = [x for x in mini]
    rem = st - sum(mini)
    for j in range(n):
        if rem <= 0:
            break
        else:
            if res[j] + rem <= maxi[j]:
                res[j] += rem
                rem = 0
            else:
                res[j] = maxi[j]
                rem -= maxi[j] - mini[j]
    print("YES")
    print(*res)