def cheapest_quote(n):
    prices = (3.85, 1.93, 0.97, 0.49, 0.1)
    quant = (40, 20, 10, 5, 1)
    cost = 0
    for i in range(5):
        while n >= quant[i]:
            cost += prices[i]
            n -= quant[i]
    return round(cost, 2)