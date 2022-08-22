from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Idade da {}a pessoa:'.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(date.today().year - ano)
print('Ao todo tiveram {} pessoas com maioridade! '.format(maior))
print('Ao todo tiveram {} pessoas com menoridade! '.format(menor))

