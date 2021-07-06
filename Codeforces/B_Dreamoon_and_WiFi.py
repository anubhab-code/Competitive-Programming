from math import pow
fact = [1]
for i in range(1,11):
    fact.append(fact[-1]*i)
s = input()
s1 = input()
n = s.count('+')
n1 = s1.count('+')
if n1 > n:
    print(0) 
else:
    extra = s1.count('?')
    plus = n-n1
    ans = fact[extra] // (fact[extra-plus]*fact[plus])
    ans /= (pow(2, extra))
    print(ans)