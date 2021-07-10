def check(n):
    if n==0:
        return True
    if n==1 or n==2 or n==3:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return True
        i+=1
    return False

for _ in range(int(input())):
    n=int(input())
    div=n//4
    rem=n%4
    while div and check(rem)==False:
        rem+=4
        div-=1
    if rem==15 and n%4==3:
        div+=1
    if check(rem) :
        if rem:
            print(div+1)
        else:
            print(div)
    else:
        print(-1)