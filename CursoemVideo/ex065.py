n = int(input('Digite um numero inteiro: '))
letra = str(input('Quer continuar:[S/N]')).upper()

maior = menor = soma = c = 0

while letra == 'S':
    n = int(input('Digite um numero inteiro: '))
    letra = str(input('Quer continuar:[S/N]')).upper()

    soma = soma + n
    c += 1
    if n >= maior:
        maior = n

    if n <= menor:
        menor = n

print('Media foi {}'.format(soma/c))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
