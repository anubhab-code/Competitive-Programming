def linked_sort(a_to_sort, a_linked, key=str):
    res = sorted(zip(a_to_sort, a_linked), key=key)
    for i in range(len(a_to_sort)):
        a_to_sort[i], a_linked[i] = res[i]
    return a_to_sort