from typing import Counter
s = input()
l = Counter(s)
ans = 0
for i in l:
    ans+=(l[i]*l[i])
print(ans)