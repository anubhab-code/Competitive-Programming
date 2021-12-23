from collections import defaultdict
for _ in range(int(input())):
    s=input()
    x,y=0,0
    sett=defaultdict(set)
    ans=0
    for i in s:
        tempx=x
        tempy=y
        if i=='N':
            y+=1
        elif i=='S':
            y-=1
        elif i=='E':
            x+=1
        else:
            x-=1
        if (tempx,tempy) in sett[(x,y)]:
            ans+=1
        else:
            ans+=5
            sett[(x,y)].add((tempx,tempy))
            sett[(tempx,tempy)].add((x,y))
    print(ans)