import random 
def r_p_s_cheat(choice):
    opp = {'rock':'paper','paper':'scissors','scissors':'rock'}
    opp2 = {'paper':'rock','scissors':'paper','rock':'scissors'}
    if random.randint(1,10) < 10:
        return opp[choice]
    return opp2[choice]