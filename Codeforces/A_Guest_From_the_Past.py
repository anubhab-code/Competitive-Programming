n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n<a and n<b:
    print(0)
else:
    if n>=b and b-c<=a:
        t = (n-b)//(b-c)
        t += 1
        n -= t*(b-c)
        print(t+n//a)
    else:
        print(n//a)