l=[]
r=[]
for i in range(int(input())):
    f=list(map(int,input().split()))
    l.append(f[0])
    r.append(f[1])
cl_1=l.count(1)
cl_0=l.count(0)
cr_1=r.count(1)
cr_0=r.count(0)
if cl_1<cl_0:
    c=cl_1
else:
    c=cl_0
if cr_1<cr_0:
    c+=cr_1
else:
    c+=cr_0
print(c)