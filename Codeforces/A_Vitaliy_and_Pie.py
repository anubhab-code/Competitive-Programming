n=int(input())
s=input()
l=[0]*26
ans=0
for i in s:
    if i.islower():
        l[ord(i)-97]+=1
    else:
        i=i.lower()
        if l[ord(i)-97]>0:
            l[ord(i)-97]-=1
            continue
        else:
            ans+=1
print(ans)