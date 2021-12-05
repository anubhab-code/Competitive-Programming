for _ in range(int(input())):
    a=input()
    b=input()
    s={}
    ans=0
    for i in range(26):
        s[a[i]]=i+1
    temp=[]
    for j in b:
        temp.append(s[j])
    for k in range(len(temp)-1):
        ans+=abs(temp[k]-temp[k+1])
    print(ans)