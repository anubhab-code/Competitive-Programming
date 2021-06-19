def divisible_by(numbers, divisor):
    l = []
    for i in numbers:
        if i % divisor == 0:
            l.append(i)
    return l