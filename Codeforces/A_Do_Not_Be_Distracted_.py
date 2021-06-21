for i in range(int(input())):
    check=False
    n=int(input())
    st=input()
    new=[st[0]]
    p=st[0]
    for j in range(1,n):
        if st[j]!=p:
            if st[j] in new:
                check=True
                print("NO")
                break
            else:
                new.append(st[j])
        p=st[j]
    if not check:
        print("YES")