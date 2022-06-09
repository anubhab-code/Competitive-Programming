for _ in range(int(input())):
    n=int(input())
    arr=[]
    dp={}
    for i in range(26):
        dp[i]=0
    for i in range(2*n):
        x=input()
        arr.append(x)
        for j in x:
            dp[ord(j)-97]+=1
    s=input()
    for j in s:
        dp[ord(j)-97]+=1
    for i in range(26):
        if dp[i]%2==1:
            ans=i
            break
    print(chr(ans+97))