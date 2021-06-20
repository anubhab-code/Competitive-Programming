a=input()
b=input()
ans=""
for i in range(len(a)):
    if a[i]!=b[i]:
        ans=ans+"1"
    else:
        ans=ans+"0"
print(ans)