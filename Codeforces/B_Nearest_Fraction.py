from fractions import Fraction
x,y,d=map(int,input().split())
f=Fraction(x,y).limit_denominator(d)
print(str(f.numerator)+"/"+str(f.denominator))