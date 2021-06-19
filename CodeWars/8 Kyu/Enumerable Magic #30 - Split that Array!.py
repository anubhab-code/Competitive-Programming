def partition(data, classifier_method):
    lsts = ([],[])
    for v in data:
        lsts[not classifier_method(v)].append(v)
    return lsts