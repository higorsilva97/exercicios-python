n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor> '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n2//n1
e = n1 ** n2

print('A soma é {} o Produto é {} Divisao é {:.3f}'.format(s, m, d),end=' ')
print('Divisao inteira é {} e Potencia é {} '.format(di, e))

