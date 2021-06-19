def toCsvText(array) :
   return '\n'.join(','.join(str(n) for n in lst) for lst in array)