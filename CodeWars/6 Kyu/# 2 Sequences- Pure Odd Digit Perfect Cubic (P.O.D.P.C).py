h=[]
for i in range(-434159,464159):
    j=str(i**3)
    if all(k in '13597-' for k in j):
        h.append(i**3)

def odd_dig_cubic(a, b):
    return [i for i in h if a<=i<=b]