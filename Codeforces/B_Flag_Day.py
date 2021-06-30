a,b=map(int,input().split())
l={}
for i in range(a):
    l[i+1]=0
for i in range(b):
    c,d,e=map(int,input().split())
    if l[c]==1:
        l[d],l[e]=2,3
    elif l[c]==2:
        l[d],l[e]=1,3
    elif l[c]==3:
        l[d],l[e]=1,2
    elif l[d]==1:
        l[c],l[e]=2,3
    elif l[d]==2:
        l[c],l[e]=1,3
    elif l[d]==3:
        l[c],l[e]=1,2
    elif l[e]==1:
        l[c],l[d]=2,3
    elif l[e]==2:
        l[c],l[d]=1,3
    elif l[e]==3:
        l[c],l[d]=1,2
    else:
        l[c],l[d],l[e]=1,2,3
for i in range(a):
    print(l[i+1],end=" ")