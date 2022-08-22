from random import randint
from time import sleep
def maior(* num):
    cont = maior = 0
    print('='*30)
    print('Analisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print()
    for valor in num:
        if valor > maior:
            maior = valor
    print(f'Maior {maior}')



maior(0, 2, 4, 0, 7, 6)
maior(0, 1, 4, 0, 9, 6)
maior(0, 2, 0, 5, 4)



