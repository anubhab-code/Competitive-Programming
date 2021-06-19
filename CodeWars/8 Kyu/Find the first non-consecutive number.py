def first_non_consecutive(arr):
    numbers = arr[:]
    numbers.sort()
    first = numbers[0]
    last = numbers[len(numbers)-1]+1
    for i in range(first,last):
        if i not in numbers:
            return i+1
    return None