def build_string(*args):
    lst = []
    for i in args:
        lst.append(i)
    return "I like " + ", ".join(lst) + "!"