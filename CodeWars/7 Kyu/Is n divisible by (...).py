def is_divisible(n, *args):
    return all(not n % i for i in args)