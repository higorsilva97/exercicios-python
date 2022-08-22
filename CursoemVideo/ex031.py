dis = float(input('Distancia da viagem em KM: '))

if dis <= 200:
    print('Preço da viagem é de R${} '.format(dis * 0.50))
else:
    print('Preço da viagem é de R${} '.format(dis * 0.45))

print('Boa viagem! ')
