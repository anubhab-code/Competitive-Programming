def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
for _ in range(int(input())):
    d=int(input())
    n=d+1
    while True:
        if isPrime(n):
            fp=n
            break
        else:
            n+=1
    n=fp+d
    while True:
        if isPrime(n):
            sp=n
            break
        else:
            n+=1
    print(fp*sp)



    
