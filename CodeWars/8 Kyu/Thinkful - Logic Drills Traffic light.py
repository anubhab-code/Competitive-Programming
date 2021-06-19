def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]