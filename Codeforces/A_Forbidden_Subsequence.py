from collections import defaultdict
for _ in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    check = defaultdict(int)
    for i in s1:
        check[i]+=1
    ans = list(check.keys())
    ans=sorted(ans)
    ans2 = sorted(s2)
    if not (ans2 == s2 and check["a"]>=1 and check["b"]>=1 and check["c"]>=1):
        final = sorted(s1)
        for i in final:
            print(i,end="")
        print()
    else:
        final = ""
        for i in ans:
            if not(i!="b" and i!="c"):
                pass
            if i!="b" and i!="c":
                final+=i*check[i]
            elif i=="c":
                final+=i*check[i]
                final+="b"*check["b"]
        print(final)