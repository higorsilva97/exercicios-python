from datetime import date

ano = int(input('Qual ano voce está? '))

if ano == 0:
    ano = date.today().year

if (ano % 4) == 0:

    if(ano % 100) == 0:

        if(ano % 400) == 0:
            print('O ano {} é bissexto, tem 366 dias'.format(ano))

else:
    print("O ano {} não é bissexto".format(ano))