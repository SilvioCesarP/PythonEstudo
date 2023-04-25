#Leia um numero inteiro
#Mostre se ele é par ou impar

numero = int(input('Digite um numero: '))
resultado = numero % 2
if resultado == 1:
    print('O numero é ímpar!')
else:
    print('O numero é par!')    
