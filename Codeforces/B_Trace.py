from math import pi
n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
if n%2==0:
    s=1
    ans=pi*(l[1]**2-l[0]**2)
else:
    s=0
    ans=pi*l[s]**2
s+=2
for i in range(s,n,2):
    ans+=pi*abs(l[i]**2-l[i-1]**2)
print("{0:.10f}".format(ans))