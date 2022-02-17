n = int(input())
s = list(input())
ans = []
while n!=0:
    if n%2==1:
        ans.append(s[0])
    else:
        ans.insert(0,s[0])
    s.pop(0)
    n = len(s)
print("".join(ans))