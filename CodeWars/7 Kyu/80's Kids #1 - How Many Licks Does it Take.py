def total_licks(env):    
    if env == {}: return "It took 252 licks to get to the tootsie roll center of a tootsie pop."
    cond_n = max(env.values())
    for key in env:
        if env[key] == cond_n:
            con = key  
    i = 252
    i += sum(env.values())    
    rep1 = f"It took {str(i)} licks to get to the tootsie roll center of a tootsie pop."
    rep2 = f" The toughest challenge was {con}."
    if cond_n > 0:
        return rep1 + rep2
    else:
        return rep1