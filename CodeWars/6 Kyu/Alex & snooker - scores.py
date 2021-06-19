def frame(score):
    result = [0, 0]
    for s in score.split('; '):
        a, b = (int(x.split('(')[0]) for x in s.split('-'))
        result[a < b] += 1
    return result