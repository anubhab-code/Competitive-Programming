s,k=map(int,input().split())
ls=[]
for i in str(s):
    ls.append(i)
for i in range(len(ls)):
    temp=i
    for j in range(i,len(ls)):
        if k<j-i:
            continue
        if ls[temp]<ls[j]:
            temp=j
    k-=temp-i
    l=temp
    while l>i:
        ls[l],ls[l-1]=ls[l-1],ls[l]
        l-=1
ans=''   
for i in ls:
    ans+=i
print(ans)