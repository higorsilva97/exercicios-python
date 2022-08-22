import random
from time import sleep

n = int(random.randint(0,5))
n2 = int(input('Tente advinhar qual o numero escolhido pelo PC: '))

print('Precessando...')
sleep(2)
if n == n2:
    print('Voce venceu!')
else:
    print('Voce perdeu!')

print('Seu numero {}'.format(n2))
print('Numero do PC {}'.format(n))

