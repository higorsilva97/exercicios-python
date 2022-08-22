v = float(input('Velociade do carro em Km/h: '))
if v > 80.0:
    print('Voce foi multado em R$ {:.2f}'.format((v - 80.0) * 7.0))

