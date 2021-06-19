for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    flag=0
    for i in range(n):
        for j in range(m):
            l.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            if l[i][j]=='R':
                if (i+j)%2!=0:
                    flag=1
                else:
                    flag=0
            elif l[i][j]=='W':
                if (i+j)%2!=0:
                    flag=0
                else:
                    flag=1
    if flag==0:
        for i in range(n):
            for j in range(m):
                if(i+j)%2==0:
                    l[i][j]='W'
                else:
                    l[i][j]='R'
    else:
        for i in range(n):
            for j in range(m):
                if(i+j)%2==0:
                    l[i][j]='R'
                else:
                    l[i][j]='W'
    for i in range(n):
        for j in range(m):
            print(l[i][j],end='')
        print("\n")
                

                