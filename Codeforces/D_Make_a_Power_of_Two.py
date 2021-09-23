powers=[]
def calc():
    i=1
    while i <= 1000000000000000000:
        powers.append(str(i))
        i*=2
calc()
for _ in range(int(input())):
    s=input()
    ans=float('INF')
    for p in powers:
        x=len(s)
        y=len(p)
        i,j,c=0,0,0
        while i<x and j<y:
            if s[i]==p[j]:
                j+=1
                c+=1
            i+=1
        ans=min(ans,x+y-(2*c))
    print(ans)
    
        