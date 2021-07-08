n = int(input())
s = input()
d = {'4': '322', '6': '53', '8': '7222', '9': '7332'}
ans = ''
for i in s:
    if i=='1' or i=='0':
        continue
    a = i
    if i in d:
        a = d[i]
    ans += a
ans = list(ans)
ans = sorted(ans)[::-1]
print(''.join(ans))