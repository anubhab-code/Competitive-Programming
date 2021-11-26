input=open("input.txt","r").readline
n=int(input())
l=input()
temp=[]
ans=[]
for i in range(n):
    if l[i]=='1':
        temp.append(i)
for j in range(1,len(temp)):
    ans.append(temp[j]-temp[j-1])
if len(set(ans))==1:
    open("output.txt","w").write("YES")
else:
    open("output.txt","w").write("NO")