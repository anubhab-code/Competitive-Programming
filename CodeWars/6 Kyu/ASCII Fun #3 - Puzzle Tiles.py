def puzzle_tiles(width, height):
    result = ['  ' + ' _( )__' * width]
    for i in range(height):
        if i % 2 == 0:
            result.append(' _|' + '     _|' * width)
            result.append('(_' + '   _ (_' * width)
            result.append(' |' + '__( )_|' * width)
        else:
            result.append(' |_' + '     |_' * width)
            result.append('  _)' + ' _   _)' * width)
            result.append(' |' + '__( )_|' * width)
    return '\n'.join(result)