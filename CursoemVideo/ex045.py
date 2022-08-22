from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[0] Pedra
[1] Papel
[3] Tesoura''')
jogador = int(input('Qual sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('PC VENCEU')
    else:
        print('OPÇÃO INVALIDA')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('PC VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA')

elif computador == 2: #COMPUTADOR JOGOU TESOURO
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('PC VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVALIDA')