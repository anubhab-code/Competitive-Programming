from math import gcd
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    a = len(s1)
    b = len(s2)
    ans = (a*b)//gcd(a,b)
    if s1*(ans//a)==s2*(ans//b):
        print(s1*(ans//a))
    else:
        print(-1)