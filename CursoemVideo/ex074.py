from random import randint

numeros = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
for n in numeros:
    print(f' {n}', end='')
print(f'O maior valor foi {max(numeros)} ')
print(f'O menor valor foi {min(numeros)}')
