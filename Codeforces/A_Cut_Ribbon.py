def ribbon(length,acceptable):
    dp = [float("-inf")]*(length+1)
    dp[0] = 0
    for i in range(1,length+1):
        for size in acceptable:
            if i - size >= 0:
                dp[i] = max(dp[i],1+dp[i-size])
    return dp[-1]
n,a,b,c = list(map(int,input().split()))
print(ribbon(n,[a,b,c]))