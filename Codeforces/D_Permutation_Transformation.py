final = [0]*101
def hehe(a,n,l,c):
    if n>a:
        temp = -1
        for i in range(a,n):
            if l[i]>temp:
                temp = l[i]
                ind = i
        final[temp] = c
        hehe(a,ind,l,c+1)
        hehe(ind+1,n,l,c+1)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    hehe(0,n,l,0)
    ans = []
    for i in l:
        ans.append(final[i])
    print(*ans)
    
    
    