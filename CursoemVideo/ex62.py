primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(' {} '.format(termo), end=' ')
        termo += razao
        c +=1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))

print('FIM')
print(c-1)
print(total)





