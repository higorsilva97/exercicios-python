prod = float(input('Valor do produto: '))
pagamento = int(input('Forma de pagamento: \n 1- A VISTA DINHEIRO OU CHQUE '
                      '                    \n 2- A VISTA CARTÃO'
                      '                    \n 3- 2x CARTÃO'
                      '                    \n 4- 3x ou MAIS NO CARTÃO \n   '))

if pagamento == 1:
    desconto = prod - ((prod*10)/100)
    print('Pagamento a vista com desconto de 10%: R$ {:.2f}'.format(desconto))

elif pagamento == 2:
    desconto = prod - ((prod*5)/100)
    print('Pagamento a vista no cartão com desconto de 5%: R$ {:.2f}'.format(desconto))

elif pagamento == 3:
    print('Pagamento em até 2x no cartão, preço normal, duas parcelas de R$ {:.2f}'.format(prod/2))

elif pagamento == 4:
    desconto = prod + ((prod*20)/100)
    print('Pagamento em 3x no cartão, parcelas com 20% de juros,{:.2f}'.format(desconto))






