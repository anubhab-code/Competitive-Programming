for _ in range(int(input())):
    s=input()
    e,n=0,0
    ans=0
    for i in range(len(s)):
        if s[i]=="N":
            n=1
            ans+=1
        else:
            e=1
    if ans<2 and n and e:
        print("NO")
    else:
        print("YES")