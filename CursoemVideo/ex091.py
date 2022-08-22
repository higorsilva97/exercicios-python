from random import randint
from time import sleep
from operator import itemgetter
import datetime
pessoa = dict()
anoatual = datetime.date.today()
import datetime


jogo = {'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6)}
ranking = list
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)

print('RANKING')
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v[0]} com {v[1]}')
    sleep(0.5)

print(anoatual.year)



