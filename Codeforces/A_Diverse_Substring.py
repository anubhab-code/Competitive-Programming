from typing import Counter
n = int(input())
s = input()
a = Counter(s)
flag = 1
for i in range(n-1):
    if s[i]!=s[i+1]:
        print("YES")
        print(s[i]+s[i+1])
        flag = 0
        break
if flag:
    print("NO")