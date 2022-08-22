salario = float(input('Qual o salario: '))

if salario >= 1250:
    print('Salario de {} com reaguste de 10% agora é de {}'.format(salario, salario+(salario*10)/100))
else :
    print('Salairo de {} com reaguste de 15% agora é de {}'.format(salario, salario+(salario*15)/100))
