import sys
a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
l2.sort()
x,y=0,0
f=sys.maxsize
while (x<a and y<b):
    if (abs(l1[x]-l2[y])<f):
        f=abs(l1[x]-l2[y])
    if (l1[x]<l2[y]):
        x+=1
    else:
        y+=1
print(f)