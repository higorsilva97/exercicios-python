r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+ r2:
    print('Os seguimentos acima podem formar um triangulo!')

else:
    print('Nao é possivel')



# (r2 + r3) < r1 < (r2 + r3):
# (r1 + r3) < r2 < (r1 + r3):
# r1 + r2) < r3 < (r1 + r2):(

