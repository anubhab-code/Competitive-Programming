from typing import Counter
def check(a,b):
    if a==b:
        return True
    if abs(a-b)==2:
        return True
    return False
    
for _ in range(int(input())):    
    n = int(input())
    s = input()
    flag=1
    for i in range(n//2):
        j = n-1-i
        if not check(ord(s[i])-ord('a'),ord(s[j])-ord('a')):
            flag=0
            break
    if flag:
        print("YES")
    else:
        print("NO")