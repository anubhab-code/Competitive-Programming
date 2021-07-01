num = list(input())
temp = -1
for i in range(len(num)):
    if int(num[i])%2 == 0:
        temp = i
        if int(num[i]) < int(num[-1]):
            break
ans = "-1"
if temp != -1:
    num[-1], num[temp] = num[temp], num[-1]
    ans = ''.join(num)
print(ans)