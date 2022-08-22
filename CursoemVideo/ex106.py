def opcoes(msg):
    titulo(msg)
    help(msg)

def titulo(msg):
    print('-'*len(msg))

    print('-' * len(msg))

while True:

    opcao = str(input('Função ou biblioteca: '))
    if opcao.upper() == 'FIM':
        break
    else:
        opcoes(opcao)
print('fim')