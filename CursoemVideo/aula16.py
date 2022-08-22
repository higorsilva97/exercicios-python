lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#uplas são imutaveis
#print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba ')

a = (1, 2, 5)
b = (4, 2, 4, 4)
c = a+b
print(c)
print(c.index(4))

pessoa = ('Higor', 25, 'M', 94)
del (pessoa)
print(pessoa)