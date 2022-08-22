peso = float(input('Peso: '))
altura = float(input('Altura: '))


imc = peso / (altura ** 2)
print('O IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso - IMC {:.2f}'.format(imc) )

elif 18.5 <= imc < 25:
    print('Peso ideal - IMC {:.2f}'.format(imc))

elif 25 <= imc < 30:
    print('Sobrepeso = IMC {:.2f}'.format(imc))

elif 30 <= imc < 40:
    print('Obesidade - IMC {:.2f}'.format(imc))

elif imc >= 40:
    print('Obesidade morbida - IMC {:.2f}'.format(imc))
