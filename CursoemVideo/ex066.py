s = c = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} numeros foi {s} ')
