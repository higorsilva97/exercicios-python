n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#VERIFICANDO MENOR
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

#VERIFICANDO MAIOR
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3

print('O numero {} é o menor'.format(menor))
print('O numero {} é o maior'.format(maior))

"""if n1 >= n2:

    if n1 >= n3:
        print('o numero {} é o maior'.format(n1))
else:

    if n2 >= n3:

        if n2 >= n1:

            print('o numero {} é o maior'.format(n2))
    else:
        if n3 >= n1:

            if n3 >= n2:

                print('o numero {} é o maior'.format(n3))"""


