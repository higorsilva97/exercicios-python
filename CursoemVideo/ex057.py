sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
masc = 'M'
femin = 'F'

while sexo != masc and sexo != femin:
    sexo = str(input('Dados invalidos, digite novamente o sexo [M/F]: ')).upper().strip()

if sexo == masc:
    print('Sexo masculino registrado com sucesso')
else:
    print('Sexo feminino registrado com sucesso')
print('FIM')