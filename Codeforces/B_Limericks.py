n = int(input())
j=2
while n%j!=0: 
    j+=1
ans=str(j)+str(n//j)
print(int(ans))