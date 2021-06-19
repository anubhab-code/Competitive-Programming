def numberToOrdinal(n):
    if n == 0:
        return "0"
    if 11 <= n % 100 <= 13 or (n % 10 not in {1,2,3}):
        return str(n) + "th"
    if n % 10 == 1:
        return str(n) + "st"
    if n % 10 == 2:
        return str(n) + "nd"
    if n % 10 == 3:
        return str(n) + "rd"