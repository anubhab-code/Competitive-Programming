def remove_smallest(n, arr):
    arr_c = arr.copy()
    if  0<n<len(arr):
        for i in sorted(arr)[:n]:
            arr_c.remove(i)
        return arr_c
    elif n <= 0:
        return arr
    else:
        return []