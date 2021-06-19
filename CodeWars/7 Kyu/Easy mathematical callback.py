def process_array(arr, callback):
    new_arr = [callback(x) for x in arr]
    return new_arr