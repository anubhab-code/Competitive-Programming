a = input().lower()
b = input().lower()
f = 0
for i in range(len(a)):
    if ord(a[i]) == ord(b[i]):
        continue
    elif ord(a[i]) > ord(b[i]):
        f = 1
        break
    elif ord(a[i]) < ord(b[i]):
        f = -1
        break
print(f)