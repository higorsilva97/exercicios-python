primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = 0
c = 0

while c != 10:
    termo = primeirotermo + razao * c
    c +=1
    print(' {} '.format(termo),end=' ')

print(c)

