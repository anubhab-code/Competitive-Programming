def find_average(array):
    sum=0
    for i in array:
        sum+=i
    return int(sum/len(array))