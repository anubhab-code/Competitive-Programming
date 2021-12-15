from typing import Counter
for _ in range(int(input())):
    a=input()
    s=Counter(a)
    if s['A']+s['C']==s['B']:
        print("YES")
    else:
        print("NO")
