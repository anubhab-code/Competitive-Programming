for _ in range(int(input())):
    n=int(input())
    s=input()
    dr=0
    win=0
    for i in range(n):
        if s[i]=='1':
            dr+=1
        else:
            win+=1
    if win>0 and win<3:
        print('NO')
        continue
    a=[]
    for i in range(n):
        l=['a']*n
        a.append(l)
    for i in range(n):
        for j in range(n):
            if i==j:
                a[i][j]='X'
            elif s[i]=='2' and s[j]=='2' and a[j][i]!='+':
                a[i][j]='+'
                a[j][i]='-'
                break
    ok=0
    for i in range(n):
        c=0
        for j in range(n):
            if s[i]=='1' and a[i][j]=='-':
                ok=1
                break
            if s[i]=='2' and a[i][j]=='+':
                c+=1
        if s[i]=="2" and c==0:
            ok=1
        if ok==1:
            break
    if ok==1:
        print('NO')
    else: 
        print("YES")
        for i in range(n):
            for j in range(n):
                if i==j:
                    print("X",end="")
                elif a[i][j]!='+' and a[i][j]!='-' and a[i][j]!='X':
                    print("=",end="")
                else:
                    print(a[i][j],end="")
            print()
