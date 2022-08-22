numeros = []
par = []
impar = []

while True:
    numeros.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar: [S/N]'))
    if resp in 'Nn':
        break

for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        par.append(numeros[c])
    else:
        impar.append(numeros[c])

print(f'A lista completa é {numeros}')
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')



for c in range(0, len(expressao)):
    if '(' in expressao[c]:
        e += 1
    if ')' in expressao[c]:
        d += 1