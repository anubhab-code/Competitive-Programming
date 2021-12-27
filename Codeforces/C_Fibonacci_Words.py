s = input()
n = len(s)
temp = []
flag = 1
for i in range(n):
    temp.append(ord(s[i])-ord('A'))
for i in range(2,n):
    if temp[i] != (temp[i-1]+temp[i-2])%26:
        flag=0
        break
if flag:
    print("YES")
else:
    print("NO")