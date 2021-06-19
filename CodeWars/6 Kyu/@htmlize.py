def htmlize(tag):
    def wrape(fn):
        def inner(*args):
            inner_txt = str(fn(*args))
            return '<{0}>{1}</{0}>'.format(tag, inner_txt)
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return inner
    return wrape