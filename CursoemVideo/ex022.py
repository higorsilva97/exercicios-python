nome = str(input('Digite o nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))


"""nome = input('Digite o nome completo: ')

maiuscula = nome.upper()
minuscula = nome.lower()
qtd = nome.split()


print('Maiusculo: ',maiuscula)
print('Minusculo: ', minuscula)
print('Quantidade de letras no nome: ',len(''.join(qtd)))
print('Quantidade de letras no primeiro nome: ', len(qtd[0]))"""









