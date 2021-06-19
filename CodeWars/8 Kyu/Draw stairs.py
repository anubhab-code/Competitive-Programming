def draw_stairs(n):
    count = 1
    res = ""
    while count < n:
        res += "I\n" + " " * count
        count += 1
    res += "I"
    return res