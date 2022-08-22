aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('-='*20)
print(f'O nome é igual a {aluno["nome"]}')
print(f'Media é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
