a = input()
b = input()
four = seven = 0
l = len(a)
for i in range(l):
    if a[i]=='4' and b[i]=='7':
        four += 1
    elif a[i]=='7' and b[i]=='4':
        seven += 1
print(max(four,seven))