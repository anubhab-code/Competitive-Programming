t=int(input())
for i in range(t):
    s=list(map(int,input().split()))
    l=sorted(s)
    if l[-1] in s[0:2]:
        if l[-2] in s[2:4]:
            print("YES")
        else:
            print("NO")
    elif l[-1] in s[2:4]:
        if l[-2] in s[0:2]:
            print("YES")
        else: 
            print("NO")
            