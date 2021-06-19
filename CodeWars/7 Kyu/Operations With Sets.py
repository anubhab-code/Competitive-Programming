def process_2arrays(arr1, arr2):
    s1,s2 = set(arr1), set(arr2)
    return [len(s1 & s2), len(s1 ^ s2), len(s1 - s2), len(s2 - s1)]