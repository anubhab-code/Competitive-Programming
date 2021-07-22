s = list(input())
d = {'(': ')', '[': ']', '<': '>', '{': '}'}
stack = []
ans = 0
c = 0
for i in s:
    if i in d.keys():
        stack.append(i)
        c += 1
    else:
        c -= 1
        if c < 0:
            print('Impossible')
            exit()
        b = stack.pop()
        if i != d[b]:
            ans += 1
if c==0:
    print(ans)
else:
    print("Impossible")