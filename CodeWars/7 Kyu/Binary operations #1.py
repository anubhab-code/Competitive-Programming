def flip_bit(value, bit_index):
    i = 1 << bit_index-1
    if value & i: 
        return value-i
    else: 
        return value+i