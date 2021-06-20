n=int(input())
s={int(i) for i in input().split()}
c=1
while(1):
    if c not in s:
        print(c)
        break
    c+=1