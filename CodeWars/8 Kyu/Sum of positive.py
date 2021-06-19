def positive_sum(arr):
    sum = 0
    for ele in arr:
        if ele > 0:
            sum += ele
    return sum