n = int(input())
data = list(map(int,input().split()))
s = 0
for nuts in data:
    if nuts > 10:
        s += nuts-10
print(s)