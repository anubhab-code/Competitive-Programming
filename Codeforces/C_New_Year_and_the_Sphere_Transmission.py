def get_sum(a, d, n):
    return ((2*a+(n-1)*d)*n) >> 1

n = int(input())
divisors = set()
for d in range(1, min(n + 1, 10**5)):
    if n % d == 0:
        divisors.add(d)
        divisors.add(n//d)
ans = [get_sum(1,d,n//d) for d in divisors]
print(' '.join(str(i) for i in sorted(ans)))