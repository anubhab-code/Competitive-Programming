s=input()
dp=[]
for i in range(len(s)):
    dp.append([0,0])
if s[0].isupper():
    dp[0][1]=1
else:
    dp[0][0]=1

for i in range(len(s)):
    if s[i].isupper():
        dp[i][0]=dp[i-1][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][1])+1
    else:
        dp[i][0]=dp[i-1][0]+1
        dp[i][1]=min(dp[i-1][0],dp[i-1][1])
print(min(dp[len(s)-1][0],dp[len(s)-1][1]))