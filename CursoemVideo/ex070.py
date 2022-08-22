total = c = cont = 0
menor = 0
barato = ''

while True:
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$ '))
    resp = str(input('Deseja continuar:[S/N}]'))
    total+= preco
    cont +=1
    menor = preco

    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    if resp == 's':
        if preco >= 1000:
            c += 1
    else:
        break

print(f'Total da compra: {total}')
print(f'{c} custaram mais de R$ 1000 reais')
print(f'O produto mais barato foi {barato} e custa R${menor}')
