def is_monotone(heights):
  for i, item in enumerate(heights):
    if i > 0 and heights[i-1] > item: return False
  return True