def a(n, s="A"):
    if n < 4: return ""
    n = n - n % 2
    h, m = n * 2 - 1, n // 2
    r = []
    for i in range(n):
        t = s.rjust(n - i).ljust(n)
        r.append(t + t[-2::-1])
    r[m] = " ".join(s * (m + 1)).rstrip().center(h)
    return "\n".join(r)