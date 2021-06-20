s = input()
l = []
for i in s:
    if i not in l:
        l.append(i)
if len(l)%2!=0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")