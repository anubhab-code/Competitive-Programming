n,x0,y0=map(int,input().split())
d={}
for i in range(n):
    x,y=map(int,input().split())
    d[(x,y)]=1
ans=0
for i in d:
    if d[i]==1:
        x1=i[0]
        y1=i[1]
        if y0-y1==0:
            m1=float('inf')
        else:
            m1=(x0-x1)/(y0-y1)
        for j in d:
            x2=j[0]
            y2=j[1]
            if y0-y2==0:
                m2=float('inf')
            else:
                m2=(x0-x2)/(y0-y2)
            if m2==m1:
                d[j]=0
        ans+=1
print(ans)

# a,x,y=map(int,input().split())
# f=set()
# cx,cy=0,0
# for i in range(a):
#     xi,yi=map(int,input().split())
#     if xi-x ==0:
#         cx=1
#     elif yi-y==0:
#         cy=1
#     else:
#         s=(yi-y)/(xi-x)
#         f.add(s)
# print(len(f)+cx+cy)