def is_perfect(n):
    s = 1
    for i in range(2, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            s += q + i
    return s == n and n != 1