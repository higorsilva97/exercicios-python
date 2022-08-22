expressao = []

letras = str(input('Digite uma expressão: '))

for c in range(0, len(letras)):
    expressao.append(letras[c])

d = e = 0
for cont in range(0, len(expressao)):
    if '(' in expressao[cont]:
        e += 1
    if ')' in expressao[cont]:
        d += 1
if e == d:
    print('Expressão correta')
else:
    print('Expressão errada')

print(expressao)