lista = []
resp = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não vou adicionar!')
    resp = str(input('Deseja continuar: [S/N]')).upper().strip()
    if resp in 'Nn':
        break

print(sorted(lista))





