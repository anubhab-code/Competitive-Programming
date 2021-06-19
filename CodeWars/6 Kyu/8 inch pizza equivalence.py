def how_many_pizzas(n):
    ratio = (n/2.0)**2 / 4 ** 2
    pizzas = int(ratio)
    slices = round( (ratio - pizzas) * 8)
    return "pizzas: {}, slices: {}".format(pizzas, slices)