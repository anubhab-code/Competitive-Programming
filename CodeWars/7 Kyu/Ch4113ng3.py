def nerdify(txt):
    result = ""
    for char in txt:
        if char.lower() == "a":
            result += "4"
        elif char.lower() == "e":
            result += "3"
        elif char == "l":
            result += "1"
        else:
            result += char
    return result