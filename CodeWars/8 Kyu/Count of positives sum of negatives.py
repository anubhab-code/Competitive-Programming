def count_positives_sum_negatives(arr):
    neg = 0
    pos = 0
    if arr==[]:
        return []
    else: 
        for a in arr:
            if a > 0:
                pos += 1
            else:
                neg += a
        return [pos, neg]