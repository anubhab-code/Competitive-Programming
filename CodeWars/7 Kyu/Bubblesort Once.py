def bubblesort_once(l):
    res = l[:]
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[j-1] > res[j]:
                res[j], res[j-1] = res[j-1], res[j]
        return res
    return []