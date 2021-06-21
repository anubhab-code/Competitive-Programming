a=input()
b=input()
c=input()
d=input()
l=[[len(a[2:]),"A"],[len(b[2:]),"B"],[len(c[2:]),"C"],[len(d[2:]),"D"]]
l=sorted(l,key=lambda x:x[0])
c=0
m=[]
for i in range(1,4):
    if 2*l[0][0]<=l[i][0]:
        c+=1
if c==3:
    m.append(l[0][1])

c=0
for i in range(3):
    if l[3][0]>=2*l[i][0]:
        c+=1
if c==3:
    m.append(l[3][1])

if len(m)==2 or len(m)==0:
    print("C")
else:
    print(m[0])