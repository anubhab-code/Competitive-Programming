def sort_list(sort_by, lst):
    elem = lambda i: i.get(sort_by)
    return (sorted(lst, key = elem, reverse = True))