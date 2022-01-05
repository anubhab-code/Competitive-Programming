for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    for i in range(1,n):
        if i==1 and s[i]==s[i-1]:
            break
        if s[i]<=s[i-1]:
            ans+=1
        else:
            break
    res=s[:ans+1]
    print(res+res[::-1])