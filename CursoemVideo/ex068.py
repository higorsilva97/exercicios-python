from random import randint
resul = 0
cont = 0
while True:
    n = int(input('Digite um numero: '))
    jogador = str(input('Par ou Impar: [P/I] '))
    pc = randint(0, 10)
    resul = pc + n

    if jogador == 'p':
        if resul % 2 == 0:
            print(f'Voce jogou {n} e o PC {pc}, resultado {resul}, PAR')
            print('Voce ganhou!')
            print('Vamos jogar novamente...')
            cont+=1
        else:
            print(f'Voce jogou {n} e o PC {pc}, resultado {resul}, IMPAR')
            print('Voce perdeu!')
            print(f'Voce venceu {cont} vezes')
            break

    if jogador == 'i':
        if resul % 2 == 0:
            print(f'Voce jogou {n} e o PC {pc}, resultado {resul}, PAR')
            print('Voce perdeu!')
            print(f'Voce venceu {cont} vezes')
            break
        else:
            print(f'Voce jogou {n} e o PC {pc}, resultado {resul}, IMPAR')
            print('Voce ganhou!')
            print('Vamos jogar novamente...')
            cont += 1







