n = sorted(list(input()))
k = sorted(list(input()))
d = {}
ans = 0
flag = 1
for i in k:
    if i in n:
        if i not in d:
            c= n.count(i)
            b = k.count(i)
            if c>=b:
                ans+=b
            else:
                ans+=c
            d[i] = 1
    else:
        flag = 0
        break
if flag:
    print(ans)
else:
    print(-1)