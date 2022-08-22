from random import randint

num = int(input('Digite um numero de 0 a 10: '))
pc = randint(0, 10)
cont = 0

while num != pc:

    if num < pc:
        num = int(input('Mais...tente mais uma vez! '))
        cont +=1
    elif num > pc:
        num = int(input('Menos...tente mais uma vez! '))
        cont += 1

print('Parabéns, voce acertou em {} tentativas! Seu numero: {} - numero do PC {}'.format(cont, num, pc))



