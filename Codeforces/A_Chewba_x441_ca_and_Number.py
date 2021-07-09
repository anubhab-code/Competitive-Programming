n = list(input())
l = len(n)
for i in range(l-1, 0, -1):
    temp = 9-int(n[i])
    if temp<int(n[i]):
        n[i] = str(temp)
temp = 9-int(n[0])
if temp!=0 and temp<int(n[0]):
    n[0] = str(temp)
print("".join(n))