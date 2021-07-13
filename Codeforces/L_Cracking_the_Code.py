def binExp(base,power):
        res = 1
        while (power != 0):
            if ((power & 1) == 1):
                res = res* base
            base = base*base
            power >>= 1
        return res

n=  input()
num= n[0]+n[2]+n[4]+n[3]+n[1]
num= int(num)
val= str(binExp(num, 5))
print(val[-5::])