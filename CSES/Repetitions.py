s = input()
c = 0
maxm = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
        if maxm <= c:
            maxm=c
    elif s[i] != s[i+1]:
        c = 0
print(maxm+1)