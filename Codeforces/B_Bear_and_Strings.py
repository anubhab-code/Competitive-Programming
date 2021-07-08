s = input()
n = len(s)
ip = []
for i in range(n-3):
    if s[i:i+4] == "bear":
        ip.append([i,i+3])
ans = 0
l = -1
for i in range(len(ip)):
    ans += (ip[i][0]-l)*(n-ip[i][1])
    l = ip[i][0]
print(ans)