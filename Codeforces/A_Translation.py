s=input()
t=input()
c=""
for i in range(1,len(s)+1):
    c=c+s[-i]
if t==c:
    print("YES")
else:
    print("NO")