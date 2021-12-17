for _ in range(int(input())):
    n=int(input())
    s=input()
    l=-1
    r=-1
    for i in range(n-1):
        if (s[i]=='a' and s[i+1]=='b') or (s[i]=='b' and s[i+1]=='a'):
            l=i+1
            r=i+2
            break
    print(l,r)