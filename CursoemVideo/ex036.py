valorCasa = float(input('Valor da casa: '))
salarioComprador = float(input('Salario comprador: '))
anos = int(input('Em quantos anos será paga: '))

prestacao = float(valorCasa/anos)/12

if prestacao > (salarioComprador*30)/100:
    print('Empréstimo bancário negado')
else:
    print('Empréstimo aprovado!')
    print('Prestações de R${:.2f} por mes'.format(prestacao))