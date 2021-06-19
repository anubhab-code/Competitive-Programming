def expression_matter(a, b, c):
    possible= [a+b+c,a*b*c,a*b+c,a*(b+c),a+b*c,(a+b)*c]
    return max(possible)