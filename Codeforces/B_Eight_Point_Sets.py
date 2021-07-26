x=set()
y=set()
include=[]
for i in range(8):
    a,b=map(int,input().split())
    include.append((a,b))
    x.add(a)
    y.add(b)
flag=1
if len(x)!=3 or len(y)!=3:
    flag=0
else:
    notinclude=[]
    x=sorted(x)
    y=sorted(y)
    for i in x:
        for j in y:
            if (i,j) not in include:
                notinclude.append((i,j))
    if len(notinclude)>1:
        flag=0
    elif len(notinclude)==1 and notinclude[0]!=(x[1],y[1]): 
        flag=0
if flag==1:
    print("respectable")
else:
    print("ugly")