try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Problemas com os tipos de dados')
except ZeroDivisionError:
    print('Não é possivel dividir numero por 0')
except KeyboardInterrupt:
    print('O usuário não quis digitar')
else:
    print(r)
finally:
    print('volte sempre! ')

