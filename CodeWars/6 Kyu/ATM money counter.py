def atm(s):
    c,v = ''.join(i for i in s if i.isalpha()).upper(), int(''.join(i for i in s if i.isdigit()))
    vc = v
    d = VALUES.get(c)
    if not d:
        return f'Sorry, have no {c}.'
    r = []
    for i in d[::-1]:
        x,v = divmod(v,i)
        r.append(x)
    if not v:
        return ', '.join(f'{i} * {j} {c}' for i,j in zip(r,d[::-1]) if i)
    return f"Can't do {vc} {c}. Value must be divisible by {d[0]}!"