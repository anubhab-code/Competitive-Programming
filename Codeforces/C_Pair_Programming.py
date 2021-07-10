for _ in range(int(input())):
    a=input()
    k,n,m=map(int,input().split()) #x,y,z
    a=list(map(int,input().split()))+[0]
    b=list(map(int,input().split()))+[0]
    i,j= 0, 0
    ans=[]
    check=True
    while i < n or j < m:
        if a[i]<= k and i<n:
            if a[i]==0:
                k += 1
            ans.append(a[i])
            i+=1
        elif b[j] <= k and j<m:
            if b[j]==0:
                k+= 1
            ans.append(b[j])
            j+=1
        else:
            check = False
            print(-1)
            break
    if check:
        print(*ans)