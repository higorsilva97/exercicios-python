dicionario = {}
listaDicionario = list()
resp = ''
cont = 0
idadetotal = 0
media = 0.0
while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo: [M/F]'))
    idade = int(input('Idade: '))
    idadetotal += idade
    dicionario['idade'] = idade
    listaDicionario.append(dicionario)
    cont += 1
    resp = str(input('Deseja continuar: [S/N]'))

    if resp in 'Nn':
        break


print(f'Foram cadastradas {len(listaDicionario)} pessoas ')
media = idadetotal / len(listaDicionario)
print(f'Media de idade foi de {idadetotal/cont} anos')
print(f'Mulheres cadastradas')

for m in listaDicionario:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]}', end=' ')
    print()

print('Lista de pessoas que estão acima da média', end='')

for med in listaDicionario:
    if med[idade] > media:
        print(f'{med["nome"]}', end='')




