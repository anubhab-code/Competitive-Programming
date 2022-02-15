n=int(input())
s=input()
ans=""
for i in s:
    if len(ans)%2==0 or i!=ans[-1]:
        ans+=i
if len(ans)%2==1:
    ans=ans[:-1]
print(len(s)-len(ans))
print(ans)
    