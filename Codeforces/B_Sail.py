t,x1,y1,x2,y2 = map(int,input().split())
dire = input()

if x1 <= x2:
    dirx = "E"
else:
    dirx = "W"
adirx = abs(x1-x2)

if y1 <= y2:
    diry = "N"
else:
    diry = "S"

adiry = abs(y1 - y2)
ans = 0
flag = 0
for d in dire:
    if adirx == 0 and adiry == 0:
        print(ans)
        flag = 1
        break
    ans+=1    
    if d == dirx and adirx > 0:
        adirx-=1
    if d == diry and adiry > 0:
        adiry-=1
    
if adirx != 0 or adiry != 0:
    print(-1)
elif adirx == 0 and adiry == 0 and flag == 0:
    print(ans)