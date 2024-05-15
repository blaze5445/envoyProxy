""" Fermat's Factorization pesudocode
    
    FermatFactor(N): // N has to be odd
      a = ceil.sqrt(N)
      b2 = a*a-N
      while b2 is not a square:
        a = a + 1
        b2 = a*a - N
      endwhile
      return a - sqrt(b2) or a + sqrt(b2)
      
    https://en.wikipedia.org/wiki/Fermat%27s_factorization_method """

import math

def Fermat(n):
  if n % 2 != 0: #see if the number is odd or even
    return n
  else:
    return none 

def Factor(n):
  a = math.sqrt(n):
  b = (a*a)-n
  while b2 is not squre:
    a = a + 1
    b = a*a - n
  return int(a), int(b)
  
  
  
