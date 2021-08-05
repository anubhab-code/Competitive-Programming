def check(have,floor):
    if have%3 or have<0: 
        return False
    n=have//3
    need=floor*(floor-1)//2
    return n>=need
n=int(input())
ans=0
for i in range(3000000):
    have=n-(i+1)*2
    if check(have,i+1): 
        ans+=1
print(ans)