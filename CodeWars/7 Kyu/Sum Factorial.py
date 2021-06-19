def sum_factorial(lst):
    nums = sorted(lst)
    current = 1
    total = 0
    for a in range(1, nums[-1] + 1):
        current *= a
        if a in nums:
            total += current
    return total