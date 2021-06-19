def memoize(func):
    map = {}
    def memoized(x):
        if x not in map:
            val = func(x)
            map[x] = val
        return map[x]
    memoized.__name__ = func.__name__
    memoized.__doc__ = func.__doc__
    return memoized