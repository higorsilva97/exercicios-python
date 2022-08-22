import math

oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))

#ipo = float(math.sqrt(math.pow(oposto,2) + math.pow(adjacente,2)))
hipo = math.hypot(oposto,adjacente)

print('{:.2f}'.format(hipo))