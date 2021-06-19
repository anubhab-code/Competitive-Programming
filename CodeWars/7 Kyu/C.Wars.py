def initials(name):
    xs = name.split()
    xs[:-1] = [x[0].upper() for x in xs[:-1]]
    xs[-1] = xs[-1].capitalize()
    return '.'.join(xs)