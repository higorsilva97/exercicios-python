import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de  {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de  {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos  {moeda.aumentar(p)}')
print(f'Diminuindo 10%, temos  {moeda.diminuir(p)}')