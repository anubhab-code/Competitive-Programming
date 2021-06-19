def contain_all_rots(strng, arr):
    return all(strng[i:] + strng[:i] in arr for i in range(len(strng)))