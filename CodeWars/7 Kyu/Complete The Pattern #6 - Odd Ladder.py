def pattern(n):
    return '\n'.join(str(i) * i for i in xrange(1, n + 1, 2))