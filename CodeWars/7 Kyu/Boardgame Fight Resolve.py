def fight_resolve(defender, attacker): 
  fight = defender+attacker
  defenders = ["ka", "sp", "as", "pk"]
  if fight.isupper() or fight.islower():
    return -1
  else:
    fighting = fight.lower()
    if fighting in defenders:
      return defender
    else:
      return attacker