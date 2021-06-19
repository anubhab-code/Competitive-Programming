def index(array, n):
    if (len(array)-1) >= n:
        return array[n]**n 
    else:
        return -1