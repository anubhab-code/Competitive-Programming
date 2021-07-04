l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
l=sorted(l)
ans=n
c=n//2
for j in range(n//2):
    while True:
        if 2*l[j]<=l[c]:
            ans-=1
            c+=1
            break
        else:
            c+=1
        if c==n:
            break
    if c==n:
        break
print(ans)
    