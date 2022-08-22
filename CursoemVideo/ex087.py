matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna =  0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

        somacoluna += matriz[l][2]
        maior = matriz[1][c]
        if maior > matriz[1][c]:
            maior = matriz[1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'Soma de todos os valores pares {somapar}')
print(f'Soma da terceira coluna : {somacoluna}')
print(f'Maior valor da segunda linha: {maior}')