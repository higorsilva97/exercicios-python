import math
num = int(input('Digite um numero: '))
f = 1
c = num
while c > 0:
    print('{} x '.format(c), end='')
    f *= c
    c -= 1
print('= {} '.format(f))