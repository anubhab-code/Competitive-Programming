def inner_join(arrA, arrB, indA, indB):
    x = []
    for i in arrA:
        for j in arrB:
            if i[indA] == j[indB] and not i[indA]==j[indB]==None:
                x.append(i+j)
    return x