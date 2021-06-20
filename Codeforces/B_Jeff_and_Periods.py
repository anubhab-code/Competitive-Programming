n= int(input())
t = list(map(int,input().split()))
u=[]
f={}
p=0
for j in range(n):
    if t[j] not in f:
        f[t[j]]=[0,j]
    else:
        if f[t[j]][0]==0:
            f[t[j]][0]= j-f[t[j]][-1]
            f[t[j]].append(j)
        elif f[t[j]][0]!='a':
            if j-f[t[j]][-1]==f[t[j]][0]:
                f[t[j]].append(j)
            else:
                f[t[j]][0]='a'
                p+=1
print(len(set(t))-p)
for j in sorted(list(f.keys())):
    if f[j][0]!='a':
        print(j,f[j][0])