l=[int(i) for i in input()]
d={}
for i in l:
    if i==4 or i==7:
        try:
            d[i]+=1
        except:
            d[i]=1
if len(d)==0:
    print(-1)
elif len(d)==1:
    print(*list(d.keys()))
else:
    if d[4]>=d[7]:
        print(4)
    else:
        print(7) 