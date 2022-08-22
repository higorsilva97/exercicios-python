nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = float(nota1+nota2)/2

if media < 5:
    print('REPROVADO!')

elif 5 < media < 6.9:
    print('RECUPERAÇÃO!')

elif media > 7.0:
    print('APROVADO! ')


print(media)



