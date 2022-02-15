n=int(input())
s=input()
b,w=[],[]
for i in range(n):
    if s[i]=="B":
        b.append(i)
    else:
        w.append(i)
if len(b)==0 or len(w)==0:
    print(0)
    exit()
ans=[]
if len(b)%2==0:
    for i in range(0,len(b),2):
        for j in range(b[i],b[i+1]):
            ans.append(j+1)
    print(len(ans))
    print(*ans)
elif len(w)%2==0:
    for i in range(0,len(w),2):
        for j in range(w[i],w[i+1]):
            ans.append(j+1)
    print(len(ans))
    print(*ans)
else:
    print(-1)