def wraps(func):
    def deco(f):
        f.__name__ = func.__name__
        f.__doc__ = func.__doc__
        return f
    return deco