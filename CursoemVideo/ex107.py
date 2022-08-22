

dinheiro = float(input('Digite um valor: R$ '))
print(f'A metade de R$ {dinheiro} é {moeda.metade(dinheiro)}')
print(f'O dobro de R$ {dinheiro} é {moeda.dobro(dinheiro)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(dinheiro)}')
print(f'Diminuindo 10%, temos R$ {moeda.diminuir(dinheiro)}')