n=int(input())
ans=''
flag=0
for i in range(n):
    s=input()
    ans+='<3'+s
ans+='<3'
s=input()
j=0
for i in range(len(ans)):
    while j<len(s) and s[j]!=ans[i]:
        j+=1
    if j==len(s):
        flag=1
        break
    j+=1
if flag==0:
    print("yes")
else:
    print("no")