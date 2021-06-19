def cube_checker(volume, side):
    if side>0 and volume>0:
        return True if side*side*side==volume else False
    else:
        return False