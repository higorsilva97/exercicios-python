valores = []
for cont in range(0, 4):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei os valores {v} ')
print('FIM')
