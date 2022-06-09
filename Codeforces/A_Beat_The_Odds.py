for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    odd,eve=0,0
    for i in l:
        if i%2==0:
            eve+=1
        else:
            odd+=1
    ans=min(odd,eve)
    print(ans)