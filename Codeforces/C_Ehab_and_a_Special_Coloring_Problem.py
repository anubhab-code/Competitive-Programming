import math
def primeFactors(n): 
        primes=[]
        while n % 2 == 0: 
            primes.append(2) 
            n = n // 2
        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                primes.append(i) 
                n = n // i 
        if n > 2: 
            primes.append(n)
        return primes
primes=[]
def SieveOfEratosthenes(n):
    global primes
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime

prime=SieveOfEratosthenes(10**5+1)

n=int(input())
ans=[1]*(n+1)
j=2
for i in range(3,n+1):
    if prime[i]:
        ans[i]=j
        j+=1
    else:
        primes=primeFactors(i)
        primes=sorted(primes)
        ans[i]=ans[primes[0]]
print(*(ans[2:]))