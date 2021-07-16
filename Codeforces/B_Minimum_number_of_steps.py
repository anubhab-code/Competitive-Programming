s=input()[::-1]
ans=0
r=0
for i in s:
    if i=="b":
        r+=1
    else:
        ans+=r
        r*=2
        r%=1000000007
print(ans%1000000007)