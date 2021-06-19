def types(x):
    if type(x) is int:
        return 'int'
    elif type(x) is str:
        return 'str'
    elif type(x) is float:
        return 'float'
    else:
        return 'bool'