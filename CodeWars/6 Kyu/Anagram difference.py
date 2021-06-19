def anagram_difference(w1, w2):
    for i in w1:
        if i in w2:
            w1 = w1.replace(i,"", 1)
            w2 = w2.replace(i,"", 1)
    return len(w1)+len(w2)