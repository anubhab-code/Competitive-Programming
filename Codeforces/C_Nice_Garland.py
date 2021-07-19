n=int(input())
s=input()
l=["RGB","RBG","GRB","GBR","BGR","BRG"]
mn=10**10
ans=""
for i in l:
    t=i
    t=t*((n+3)//3)
    t=t[0:n]
    c=0
    for j in range(n):
        if t[j]!=s[j]:
            c+=1
    if c < mn:
        mn=c
        ans=t
print(mn)
print(ans)