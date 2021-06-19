def calculator(a, b, c):
    a, b = a / 5, b / 8 + c / 5
    return "Walk" if a < 2 and a <= b or a < 1 / 6 else "Bus"