for _ in range(int(input())):
    s=input()
    o,e,c1,c2=0,0,0,0
    flag=0
    for i in range(len(s)):
        if i%2==0:
            if s[i]=='1':
                e+=1
            elif s[i]=='?':
                c1+=1
        else:
            if s[i]=='1':
                o+=1
            elif s[i]=='?':
                c2+=1
        if o+c2 > e + (9-i)//2:
            print(i+1)
            flag=1
            break
        if e+c1 > o + (10-i)//2:
            print(i+1)
            flag=1
            break
    if not flag:
        print(10)