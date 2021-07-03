def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

n = int(input())
if isprime(n):
	print(1)
elif isprime(n-2):
	print(2)
elif n%2 == 0:
	print(2)
else:
	print(3)