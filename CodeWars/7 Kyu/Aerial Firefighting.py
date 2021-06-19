from math import ceil 

def waterbombs(arr, w):
  fires = "".join(arr).split('Y')
  bombs = 0
  for fire in fires:
      bombs += ceil(len(fire)/w)
  return bombs