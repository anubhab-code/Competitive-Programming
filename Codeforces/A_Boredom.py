n = int(input())
dp = [0]*100001
l = list(map(int,input().split()))
for i in l:
    dp[i] += i 
ans, b = 0, 0
for i in dp:
    ans,b = max(ans,i+b),ans
print(ans)