for _ in range(int(input())):
    s=input()[::-1]
    t=input()[::-1]
    i=0
    j=0
    while j<len(s):
        if i==len(t):
            break
        if s[j]==t[i]:
            i+=1
        else:
            j+=1
        j+=1
    if i==len(t):
        print("YES")
    else:
        print("NO")