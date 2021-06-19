def comfortable_word(w):
  
  left = ["t", "g", "b", "v", "f", "r", "e", "d", "c", "w", "s", "x", "q", "a", "z"]
  
  for a in range(len(w)-1):
    if w[a] in left and w[a+1] in left:
      return False
      break
    elif w[a] not in left and w[a+1] not in left:
      return False
  return True