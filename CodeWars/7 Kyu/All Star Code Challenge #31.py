def help_jesse(arr):
    l = []
    for item in arr:
        s = 'Pour {} mL of {} into a {}'.format(item.amount, item.solution, item.instrument)
        try:
            s+= ' ({})'.format(item.note)
        except AttributeError:
            pass
        l.append(s)
    return l