def metade(d=0,taxa = 0,  formato=False):
    res = d/2
    return res if not formato else moeda(res)



def dobro(d, formato=False):
    res = d*2
    return res if not formato else moeda(res)


def aumentar(d=0, formato=False):
    aumento = 0
    aumento = (d*10)/100
    aumento += d
    return aumento if not formato else moeda(aumento)


def diminuir(d=0, formato=False):
    dimin = 0
    dimin = (d *10) / 100
    dimin -= d
    return dimin if not formato else moeda(dimin)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')

def resumo(preco, a, r):
    print('*'*30)
    print('RESUMO DO VALOR')
    print('*' * 30)
    print(f'Preço analisado {preco}')
    print(f'Dobro do preço {dobro(preco)}')
    print(f'Metade do preço {metade(preco)}')
    print(f'Aumento de {a}, temos {aumentar(preco, a)}')
    print(f'Dimuição de {a}, temos {diminuir(preco, )}')




