#alunos = []
#notas = []
#temp = []
#tempnotas = []
#media = n1 = n2 = 0.0

# True:
  #  temp.append(str(input('Nome do aluno: ')))
  #  n1 = (float(input('Nota 1: ')))
   # n2 = (float(input('Nota 2: ')))
   # media = (n1 + n2)/2
   # tempnotas.append(temp[:])
   # tempnotas.append(n1)
   # tempnotas.append(n2)
  #  temp.append(media)
  #  notas.append(tempnotas[:])
  #  alunos.append(temp[:])
 #   temp.clear()
 #   tempnotas.clear()
 #   resp = str(input('Deseja continuar: [S/N]'))
 #   if resp in 'Nn':

 #       break
#print('='*30)
#print('No. Nome     Media')
#for i in range(0, len(alunos)):
   # print(f'{i} {alunos[i]}')

#while True:
   # respaluno = int(input('Deseja ver a nota de qual aluno:(999) enterrompe  '))
  #  if respaluno == 999:
  #      print('Finalizado')
  #      break
  #  else:
  #      print(f'As notas de {notas[respaluno][0]} foram {notas[respaluno][1]} e {notas[respaluno][2]}')
while True:
    ficha = list()
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar: [S/N]'))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*20)
    opc = int(input('Mostrar nota de qual aluno: '))
    if opc == 999:
        print('FINALIZADO')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
