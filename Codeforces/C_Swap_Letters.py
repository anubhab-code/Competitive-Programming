from collections import deque
n=int(input())
s=list(input())
t=list(input())
a=deque([])
b=deque([])
diff=0
x=[]
for i in range(n):
    if s[i]!=t[i]:
        diff+=1
        x.append(i)
if diff%2!=0:
    print(-1)
elif diff==2:
    print(2)
    print(x[0]+1,x[0]+1)
    print(x[0]+1,x[1]+1)
else:
    for i in range(0,n):
        if t[i]!=s[i]:
            if t[i]=='a':
                a.append(i)
            else:
                b.append(i)
    total=0
    steps=[]
    for i in range(0,len(a)//2):
        steps.append((a[i]+1,a[len(a)-1-i]+1))
    for i in range(0,len(b)//2):
        steps.append((b[i]+1,b[len(b)-1-i]+1))
    if len(a)%2==len(b)%2==1:
        steps.append((a[len(a)//2]+1,a[len(a)//2]+1))
        steps.append((a[len(a)//2]+1, b[len(b)//2]+1))
    print(len(steps))
    for i in steps:
        print(*i)