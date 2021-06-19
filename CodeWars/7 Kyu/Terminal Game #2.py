def move(self, dir):
    position = int(self.position)
    if dir == "up":
        position -= 10
    elif dir == "down":
        position += 10
    elif dir == "left":
        position -= 1
    else:
        position += 1
    if position < 0 or position > 44 or position % 10 > 4:
        raise Exception("Invalid direction")
    self.position = '{:02d}'.format(position)
    
Hero.move = move