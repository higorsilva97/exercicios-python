

def leiaInt(msg):
    while True:
       try:
           n = int(input(msg))
       except(ValueError, TypeError):
            print('Erro de valores, digite um valor inteiro valido')
            continue
       except KeyboardInterrupt:
           print('Usuario nao digitou')
           return 0
       else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Erro de tipo, coloque um valor real valido')
            continue
        except KeyboardInterrupt:
            print('Usuario não digitou nada! ')
            return 0
        else:
            return n


n = leiaInt('Digite um humero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'Voce acabou de digitar o numero inteiro {n}')
print(f'Voce acabou de digitar o numero real {n2}')