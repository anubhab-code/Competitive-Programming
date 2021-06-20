n=int(input())
l1=list(map(int,input().split()))
ans=0
for i in l1:
    ans=ans+float(i/100)
s2=float((ans/n)*100)
print(s2)