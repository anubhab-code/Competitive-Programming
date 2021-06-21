n=int(input())
final=[]
given=list(map(int,input().split()))
for i in range(1,n-1):
    l=[]
    j=0
    while j!=n-1:
        if j+1==i:
            l.append(given[i+1]-given[j])
            j+=2
        else:
            l.append(given[j+1]-given[j])
            j+=1
    final.append(max(l))
print(min(final))