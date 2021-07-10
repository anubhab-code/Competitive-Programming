for _ in range(int(input())):
    s=input()
    check=True
    n=len(s)
    for i in range(n,0,-1):
        if ord(s[0])==(96+i):
            s=s[1:]
        elif ord(s[-1])==(96+i):
            s=s[:-1]
        else:
            check=False
            print("NO")
            break
    if check:
        print("YES")