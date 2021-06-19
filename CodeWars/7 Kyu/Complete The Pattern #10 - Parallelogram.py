from string import digits

OUTPUT = '{}{}{}'.format
def pattern(n):
    nums = ''.join(digits[a % 10] for a in range(1, n + 1))
    return '\n'.join(OUTPUT(' ' * (n - a), nums, ' ' * (a - 1)) for a in range(1, n + 1))