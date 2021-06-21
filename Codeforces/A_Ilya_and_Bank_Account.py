n = int(input())
if n >=0 :
    print(n)
else:
    number = [x for x in str(n)]
    tt = number[:-2]+list(number[-1])
    t1 = int(''.join(number[:-1]))
    t2 = int(''.join(tt))
    print(max(t1,t2))