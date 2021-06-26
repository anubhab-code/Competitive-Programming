from typing import Counter
f=open("input.txt","r")
f=f.read().split("\n")
a,b=map(int,f[0].split())
k=1
c={}
l=[]
for _ in f[1].split():
    i=int(_)
    c[i]=c.get(i,[])
    c[i]+=[k]
    k+=1
    l.append(i)
l.sort()
ll=[]
cc=Counter(l[-b:])
f=open("output.txt","w")
f.write(str(l[-b])+"\n")
for i in list(cc.keys()):
    ll+=c[i][:cc[i]]
ll.sort()
for i in ll:
    f.write(str(i)+" ")