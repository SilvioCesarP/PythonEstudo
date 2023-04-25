
#gerar um numero inteiro aleatorio entre 1 e 5
#Leia um numero
#Mostre se acertou ou não o numero comparado ao numero gerado

import random

num_aleatorio = random.randint(1,5)
numero = int(input('Digite um numero aleatorio entre 1 e 5: '))

if numero == num_aleatorio:
    print('VOCE ACERTOU O NUMERO! PARABENS!')
elif numero < 1 or numero > 5:
    print('NUMERO INVÁLIDO!')
else:
    print('INFELIZMENTE ERROU! TENTE UMA PROXIMA VEZ')
