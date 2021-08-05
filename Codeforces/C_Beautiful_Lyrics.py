vowels = 'aeoiu'
d = {}
d2 = {}
n = int(input())
pairs1 = []
pairs2 = []
for i in range(n):
    w = input()
    cnt = 0
    lst = '-'
    for c in w:
        if c in vowels:
            lst = c
            cnt += 1
    key = str(cnt)+lst
    if key in d:
        pairs2.append((w, d[key]))
        del d[key]
    else:
        d[key] = w
 
for k in d:
    k2 = k[:-1]
    if k2 in d2:
        pairs1.append((d[k], d2[k2]))
        del d2[k2]
    else:
        d2[k2] = d[k]
l2 = len(pairs2)
 
r1 = min(len(pairs1), l2)
r2 = (l2 - r1) // 2
r2 = r2 if r2 >= 0 else 0
print(r1+r2)
for i in range(r1):
    print(pairs1[i][0], pairs2[i][0])
    print(pairs1[i][1], pairs2[i][1])
j = r1
while j + 1 < l2:
    print(pairs2[j][0], pairs2[j+1][0])
    print(pairs2[j][1], pairs2[j+1][1])
    j += 2