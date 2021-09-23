n = int(input())
sher = sorted(input())
mori = sorted(input())
x,y = 0,0
for i in mori:
    if i >= sher[x]:
        x+=1
    if i > sher[y]:
        y+=1
print(n-x)
print(y)