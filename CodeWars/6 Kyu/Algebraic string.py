def sum_prod(strexpression):
    s = 0
    for element in strexpression.split('+'):
        element = element.strip()
        if '*' in element:
            prod = 1
            for part in element.split('*'):
                prod *= float(part)
            s += prod
        else:
            s += float(element)
    return "%.5e"%s