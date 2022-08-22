print('-' *40)
print('LISTAGEM DE PREÇOS')
print('-' *40)

produto = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno',
           15.90, 'Estojo',25.00, 'Transferidor',4.20,'Compasso',
           9.99,'Mochila',120.32, 'Canetas',22.30, 'Livros', 34.90)

for pos in range(0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<30}',end='')
    else:
        print(f'R${produto[pos]:>7.2f}')
