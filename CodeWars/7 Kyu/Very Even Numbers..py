def is_very_even_number(n):
    while n>=10:
        p, n = n, 0
        while p>0:
            rep = p%10
            n += rep
            p //= 10
    return n%2==0