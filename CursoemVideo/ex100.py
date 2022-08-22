from random import randint

numeros = []
def sorteia():

    print('Sorteando 5 valores da lista...', end='')
    for i in range(0, 5):
        numeros.append(randint(0, 10))
    print(numeros)


def somaPar():
    soma = 0
    for i in range(0, 5):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f'Soma dos numeros pares foi {soma}')


sorteia()
somaPar()
