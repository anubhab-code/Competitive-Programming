def reverse_and_mirror(s1, s2):
    return (s2[::-1] + '@@@' + s1[::-1] + s1).swapcase()