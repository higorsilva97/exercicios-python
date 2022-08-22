n = int(input('Digite um numero: '))
c = 0
soma = 0

while n != 999:
    soma = soma + n
    n = int(input('Digite um numero: '))
    c += 1

print('Soma: {}'.format(soma))
print('Foram somados {} '.format(c))
print('FIM')
