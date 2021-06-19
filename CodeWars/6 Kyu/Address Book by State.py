def by_state(a):
    R = {}
    for l in [l for l in a.split('\n') if l]:
        ll, ss = l.replace(',', '').rsplit(' ', 1)
        ss = {'AZ': 'Arizona', 'CA': 'California', 'ID': 'Idaho', 'IN': 'Indiana', 'MA': 'Massachusetts',
              'OK': 'Oklahoma', 'PA': 'Pennsylvania', 'VA': 'Virginia'}[ss]
        R[ss] = R.get(ss, []) + ['..... ' + ll + ' ' + ss]

    r = []
    for ss in sorted(R.keys()):
        r += [' ' + ss] + [l for l in sorted(R[ss])]
            
    return '\r\n'.join(r).strip()