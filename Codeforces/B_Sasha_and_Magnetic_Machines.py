n = int(input())
l = list(map(int,input().split()))
mi = min(l)
s = sum(l)
a = set(l)
ans = 0
for i in a :
    d = 2
    while i//d>mi:
        if i%d == 0:
            sub = i//d + mi*d - i - mi
            x = min(ans,sub)
        d += 1
print(ans+s)