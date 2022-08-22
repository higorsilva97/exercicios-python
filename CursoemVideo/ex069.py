maior = homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    cont = str(input('Quer continuar [S/N]'))

    if cont == 's':
        if idade > 18:
            maior += 1

        if sexo == 'm':
            homem += 1

        if sexo == 'f' and idade > 20:
            mulher += 1

    else:
        break

print(f'{maior} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'{mulher} tem menos de 20 anos')


