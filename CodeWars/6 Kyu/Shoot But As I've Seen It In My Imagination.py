import math

def find_prob(balls_set, event):
    possible = True
    num = 1
    den = 1
    balls = dict()
    available_ball = len(balls_set)
    for b in balls_set:
        if b in balls:
            balls[b] += 1
        else:
            balls[b] = 1
    for e in event:
        lc = ABBREVIATIONS[e]
        if lc not in balls or balls[lc] == 0:
            possible = False
            break
        num *= balls[lc]
        den *= available_ball
        balls[lc] -= 1
        available_ball -= 1
        g = math.gcd(num, den)
        den //= g
        num //= g
    
    if possible:
        return [num, den]
    else:
        return ["Impossible"]