import datetime

anonasci = int(input('Ano de nascimento:  '))
ano = datetime.date.today().year
idade = ano - anonasci
print('Quem nasceu em {} tem {} anos em {}'.format(anonasci,idade,ano))

if (idade) > 18:
    print('Já passou do tempo de se alistar!')

elif (idade) == 0:
    print('Se aliste agora!')

elif (idade) < 18:
    print('Voce ainda vai se alistar!, faltam {} anos '.format(idade))

print('Idade: ', idade)
