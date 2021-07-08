s1=input()
s2=input()
ans=""
c=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        ans+=s1[i]
    else:
        c+=1
        if c%2==0:
            ans+=s1[i]
        else:
            ans+=s2[i]
if c%2==0:
    print(ans)
else:
    print("impossible")
    