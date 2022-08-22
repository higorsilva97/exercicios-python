def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um numero inteiro valido!')
        if ok:
            break
    return valor



n = leiaInt('Digite um humero: ')
print(f'Voce acabou de digitar o numero {n}')
