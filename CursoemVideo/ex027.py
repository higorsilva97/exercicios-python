nome = str(input('Digite o nome completo: '))
primeio = nome.split()

print('Nome: {} '.format(nome))
print('Primeiro nome: {} '.format(primeio[0]))
print('Ultimo nome:{} '.format(primeio[len(primeio)-1]))

