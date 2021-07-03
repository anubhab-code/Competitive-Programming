n,m = map(int,input().split())
s = ['$'] + [*input()] + ['$']
ans = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] == '.':
        ans+=1
for i in range(m):
    a,b = input().split()
    a = int(a)
    if s[a] == b == '.':
        print(ans)
    elif s[a] != '.' and b!= '.':
        print(ans)
    elif s[a] == '.':
        if s[a-1] == '.':
            ans-=1
        if s[a+1] == '.':
            ans-=1
        print(ans)
        s[a] = b
    else:
        if s[a-1] == '.':
            ans+=1
        if s[a+1] == '.':
            ans+=1
        print(ans)
        s[a] = b