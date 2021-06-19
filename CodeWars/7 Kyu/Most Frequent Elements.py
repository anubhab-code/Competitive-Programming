from collections import Counter

def find_most_frequent(l):
    count = Counter(l)
    m = max(count.values()) if l else None
    return set(i for i in l if count[i] == m)