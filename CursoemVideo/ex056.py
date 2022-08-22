from datetime import date

atual = date.today().year
media = 0.0
cont = 0
maior = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0

for p in range(1, 5):
    print('--------- {}a PESSOA ---------'.format(p))
    
    nome = str(input('Nome: '.format(p))).upper()
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo: '.format(p))).upper()
    cont += idade

    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

print('Media de idade do grupo é {}'.format(cont/4))
print('O homem mais velho tem {} e se chama {} '.format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos '.format(totmulher))



