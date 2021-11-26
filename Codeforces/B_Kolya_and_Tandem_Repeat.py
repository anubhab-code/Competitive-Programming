s = input()
k = int(input())
for i in range(k):
    s+='#'
n = len(s)
ans=0
for i in range(n):
    l = 1
    while n >= i+2*l:
        flag = 1
        for j in range(i,i+l):
            if s[j]!=s[j+l] and s[j]!='#' and s[j+l]!='#':
                flag = 0
                break
        if flag:
            ans = max(ans,2*l)
        l+=1
print(ans)