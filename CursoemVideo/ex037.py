import math

n = int(input('Digite um numero: '))
base = int(input('Digite em qual base de oonversão deseja ver o numero: 1-Binario 2-Hexadecimal 3-Octal: '))

if base == 1:
    binario = bin(n)
    print('Numero {} em binario é {}'.format(n, binario[2:]))

elif base == 2:
    hexa = hex(n)
    print('Numero {} em hexadecimal é {}'.format(n, hexa[2:]))

elif base == 3:
    octal = oct(n)
    print('Numero {} em octal é {}'.format(n, octal[2:]))
else:
    print('opção invalida!')