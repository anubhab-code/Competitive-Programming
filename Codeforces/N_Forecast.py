a,b,c=map(float,input().split())
d=(b*b-4*a*c)**0.5
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)
ans=[x1,x2]
ans=sorted(ans)[::-1]
print(ans[0])
print(ans[1])