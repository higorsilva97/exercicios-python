frase = str(input('Digite uma frase: ')).strip()

print('Letra A aparece {}'.format(frase.upper().count('A'),'vezes'))
print('Aparece a primeira vez na posição {} '.format(frase.upper().find('A')+1))
print('Aparece a ultima vez na posição {} '.format(frase.upper().rfind('A')+1))

