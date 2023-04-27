#Gere um numero de 0 a 10
#Leia um numero
#Compare o numero com o numero gerado
#Mostre se acertou, se errou mostre se o numero gerado é maior ou menor que o numero chutado
#Mostre quantas tentativas

import random
gerado = random.randint(0, 1)
num = int(input('Digite um numero de 0 a 10: '))
while  num != gerado:
    if num > gerado:
        print('Errou, o numero gerado é menor, TENTE DENOVO: ')
    elif num < gerado:
        print('Errou, o numero gerado é maior, TENTE DENOVO: ')
    elif num > 10 or num < 0:
        print('Numero inválido, apenas numeros inteiros e entre 0 e 10, TENTE NOVAMENTE: ')
print('ACERTOU!!!')
    