from collections import Counter, defaultdict
a=input().strip()
b=input().strip()
d=defaultdict(int)
flag=1
if(len(a)<len(b)):
    flag=0
d=Counter(b)
c=Counter(a[:len(b)])
f=1
x=0
y=0
ans=0
for i in d:
    if(i in d and c[i]==d[i]):
        continue
    elif(i in d and c[i]<d[i]):
        y+=d[i]-c[i]
    elif(i in d and c[i]>d[i]):
        f=0
    elif(i not  in d):
        f=0
if(f and c['?']==y):
    ans+=1
for j in range(len(b),len(a)):
    c[a[j-len(b)]]-=1
    c[a[j]]+=1
    f=1
    x=0
    y=0
    for i in d:
        if(i in d and c[i]==d[i]):
            continue
        elif(i in d and c[i]<d[i]):
            y+=d[i]-c[i]
        elif(i in d and c[i]>d[i]):
            f=0
        elif(i not in  d):
            f=0
    if(f and c['?']==y):
        ans+=1
if flag==0:
    print(0)
else:
    print(ans)