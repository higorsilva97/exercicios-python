
while True:
    print('------------Tabuada--------------')
    num = int(input('Digite um numero: '))
    print('-'*20)
    if num < 0:
        print('Acabou')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')





