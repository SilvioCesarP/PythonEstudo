#Gere um numero de 0 a 10
#Leia um numero
#Compare o numero com o numero gerado
#Mostre se acertou, se errou mostre se o numero gerado é maior ou menor que o numero chutado
#Mostre quantas tentativas

import random
gerado = random.randint(0, 10)
acertou = False
tent = 0
while not acertou:
    num = int(input('Digite um numero de 0 a 10: '))
    if num > gerado:
        print('Errou, o numero gerado é menor, TENTE DENOVO: ')
        tent += 1
    elif num < gerado:
        print('Errou, o numero gerado é maior, TENTE DENOVO: ')
        tent += 1
    elif num > 10 or num < 0:
        print('Numero inválido, apenas numeros inteiros e entre 0 e 10, TENTE NOVAMENTE: ')
        tent += 0
    elif num == gerado:
        acertou = True

print('ACERTOU!!! em {} tentativas'.format(tent))
    