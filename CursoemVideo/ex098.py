from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    for t in range(i, f+1, p):
        print(f'{t} ', end='')
        sleep(0.5)
    print('FIM')


print('contagem de 0 a 10')
for c in range(1, 11):
    print(f'{c} ', end='')
    sleep(0.5)
print('FIM')


print('contagem de 10 até 0 de 2 em 2 ')
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.5)
print('FIM')

print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passos = int(input('Passoa: '))
contador(inicio, fim, passos)