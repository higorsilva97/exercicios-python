matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num = 0
for l in range(0, 3):
    for c in range(0, 3):
       matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]:'))

print('=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()


