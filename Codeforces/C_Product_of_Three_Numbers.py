for _ in range(int(input())):
    n=int(input())
    ans=[]
    i=2
    while len(ans)<2 and i*i<n:
        if n%i==0:
            ans.append(i)
            n//=i
        i+=1
    if len(ans)==2 and n not in ans:
        print('YES')
        print(*ans,n)
    else:
        print('NO')