def fun(s):
    for i in range(len(s)):
        if s[i]!='1' and s[i]!='4':
            return False
    if s[0]!='1':
        return False
    if s.find('444')!=-1:
        return False
    return True

n=input()
if fun(n):
    print("YES")
else:
    print("NO")