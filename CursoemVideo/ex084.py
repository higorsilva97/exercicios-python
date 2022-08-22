pessoas = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        else:
            if dados[1] < menor:
                menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar: [S/N] '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}Kg de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ')

print(f'O menor peso fdi de `{menor}Kg de ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ')
