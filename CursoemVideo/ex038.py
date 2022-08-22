n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 > n2:
    print('Primeiro valor é o maior: {} '.format(n1))

elif n2 > n1:
    print('Segundo valor é maior: {} '.format(n2))

else :
    print('Não existe valor maior, os dois são iguais: {} e {}'.format(n1,n2))
