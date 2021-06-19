def sort_by_language(arr):
    arr=list(sorted(arr, key = lambda x : x["first_name"]))
    arr=list(sorted(arr, key = lambda x : x["language"]))
    return arr