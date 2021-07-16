l = [0,0,1,2,0,2,1]
a,b,c = map(int, input().split())
e = min(a//3,b//2,c//2)
k = 7*e
a,b,c = a-(3*e), b-(2*e), c-(2*e)
ll = [a,b,c]
ans = 0
for i in range(7):
    j = i
    lll = [] + ll
    cnt = 0
    while lll[l[j]] > 0:
        lll[l[j]] -= 1
        cnt+=1
        j += 1
        j %= 7
    ans = max(ans,cnt)
print(k+ans)