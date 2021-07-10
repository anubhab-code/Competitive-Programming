n = int(input())
s = input()
d = {}
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if s[i] == "1":
        for e in range(0,b):
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
    if s[i] == "0":
        k = b
        while k < 126:
            for j in range(k,k+a):
                if j in d:
                    d[j] += 1
                else:
                    d[j] = 1
            k += (2*a)
    else:
        k = b+a
        while k < 126:
            for j in range(k, k+a):
                if j in d:
                    d[j] += 1
                else:
                    d[j] = 1
            k += (2*a)
for i in d:
    ans = max(ans,d[i])
print(ans)