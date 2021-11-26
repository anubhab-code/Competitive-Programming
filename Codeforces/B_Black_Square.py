import sys
n,m = map(int,input().split())
l=[]
for i in range(n):
    a=input()
    l.append(a)
ans=0
mir=mic=sys.maxsize
mar=mac=-sys.maxsize
flag=0
for i in range(n):
    for j in range(m):
        if l[i][j] == 'B':
            ans-=1
            mar=max(mar,i)
            mir=min(mir,i)
            mac=max(mac,j)
            mic=min(mic,j)
check = max(abs(mar-mir),abs(mac-mic))+1
if ans==0:
    flag=0
elif check > min(n,m):
    flag=-1
else:
    flag=1
    
if flag==0:
    print(1)
elif flag==-1:
    print(-1)
else:
    ans+=check*check
    print(ans)