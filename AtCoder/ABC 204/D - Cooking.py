def findMin(a, n): 
    su = 0
    su = sum(a)
    dp = [[0 for i in range(su + 1)]
             for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, su + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, su + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
    diff = 1005
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break 
    return diff
     
n = int(input())
a = list(map(int,input().split()))

m = findMin(a, n)
print(((sum(a)-m)//2)+m)