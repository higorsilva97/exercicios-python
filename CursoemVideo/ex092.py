from datetime import datetime
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
pessoa['carteiraTrabalho'] = int(input('Carteira de trabalho: '))
pessoa['idade'] = datetime.now().year - nasc
if pessoa['carteiraTrabalho'] > 0:
    pessoa['anoContratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['anoContratacao'] + 35) - datetime.now().year

for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')


