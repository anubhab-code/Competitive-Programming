n = int(input())
coords = []
feas = []
for i in range(n):
    coords.append(tuple(list(map(int,input().split()))))
for i in coords:
    count = 0
    r = 0
    l = 0  
    u = 0
    d = 0
    for j in coords:
        if j[0] > i[0] and j[1] == i[1]:
            if l == 0:
                count += 1
                l = 1
        if j[0] < i[0] and j[1] == i[1]:
            if r == 0:
                count += 1
                r = 1
        if j[1] > i[1] and j[0] == i[0]:
            if u == 0:
                count += 1
                u = 1
        if j[1] < i[1] and j[0] == i[0]:
            if d == 0:
                count += 1
                d = 1
    if count == 4:
        feas.append(i)
print(len(feas))