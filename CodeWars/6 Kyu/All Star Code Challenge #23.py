def scoring(array):
    score = {}
    for p in array:
        total = 0
        total += p['norm_kill'] * 100
        total += p['assist'] * 50
        total += p['damage'] * 0.5
        total += p['healing'] * 1
        total += 2**p['streak']
        total += p['env_kill'] * 500
        score[p['name']] = total

    return sorted(score, key=score.get, reverse=True)