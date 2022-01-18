for _ in range(int(input())):
    n,m,r,c=map(int,input().split())
    mat=[]
    for i in range(n):
        s=input()
        mat.append(s)
    a1,a2=0,0
    for i in range(n):
        for j in range(m):
            if mat[i][j]=="B":
                a1 = 1
            if mat[i][c-1]=="B":
                a2 = 1
            if mat[r-1][j]=="B":
                a2 = 1
    if mat[r-1][c-1]=="B":
        print(0)
    elif a2==0 and a1==1:
        print(2)
    elif a1==0:
        print(-1)
    elif a1==1 and a2==1:
        print(1)