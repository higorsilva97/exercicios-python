dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))

preco = (dias*60.0) + (0.15*km)

print('Total a pagar: R$ {}'.format(preco))
