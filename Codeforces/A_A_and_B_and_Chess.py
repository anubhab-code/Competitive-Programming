d={'r':5,'b': 3,'n':3,'q':9,'p':1}
p=0
for _ in range(8):
 for i in input():
     p+=d.get(i.lower(),0)*(-1+2*i.isupper())
print('White' if p>0 else ['Black','Draw'][not p])