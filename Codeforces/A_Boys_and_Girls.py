f=open("input.txt",'r')
g=open("output.txt",'w')
a,b=map(int,f.readline().split())
ans = ''
if a<b:
    ans='GB'*min(a,b)+('G'*abs(a-b))
else:
    ans='BG'*min(a,b)+('B'*abs(a-b))
g.write(ans)