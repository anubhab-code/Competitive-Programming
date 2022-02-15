a = input()
b = input()
flag = 0
s = set()
for i in b:
    s.add(i)
s.remove(" ")
for i in a:
    if i in s:
        flag = 1
        print("YES")
        break
if not flag:
    print("NO")