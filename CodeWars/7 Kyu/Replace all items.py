def replace_all(obj, find, replace):
    lst = [ replace if find == x else x for x in obj]
    if isinstance(obj, str):
        return "".join(lst)
    else:
         return lst