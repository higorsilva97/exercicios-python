import datetime

nasc = int(input('Ano de nascimento: '))
idade = (datetime.date.today().year)-nasc

if idade <= 9:
    print('MIRIN')
elif 10 > idade <= 14:
    print('INFANTIL')
elif 14 > idade <= 19:
    print('JUNIOR')
elif 19 > idade > 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')

print(idade)
