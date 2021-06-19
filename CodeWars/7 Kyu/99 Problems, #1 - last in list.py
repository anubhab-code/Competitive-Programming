def last(lst):
    lst.reverse()
    for i in lst:
        return i
    if len(lst) == 0:
        return None