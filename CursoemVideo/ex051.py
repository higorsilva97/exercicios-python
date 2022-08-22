primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = 0
for c in range(0,10):
    termo = primeirotermo + razao*c
    print(termo, end=' - ')
print('ACABOU')