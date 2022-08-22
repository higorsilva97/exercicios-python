lista = []
resp = ''
while True:
    n = (int(input('Digite um numero: ')))
    resp = str(input('Quer continuar: [S/N]'))
    lista.append(n)
    if resp in 'Nn':
        break
if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5)} ')
else:
    print('5 Não foi digitado')
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {len(lista)} numeros')