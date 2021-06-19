from math import ceil
def digits(n):
    while n >= 10:
        if (n % 10) % 2 > 0:
            return False
        n //= 10
    return n % 2 == 0

def even_digit_squares(a, b):
    s = ceil(a ** 0.5); t = int(b ** 0.5)
    return [i * i for i in range(s, t + 1) if digits(i * i)]