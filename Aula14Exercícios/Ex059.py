#Leia 2 valores
#Motre um menu com opçoes
#Mostre o resultado
from time import sleep

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
acertou = False
while not acertou:
    resposta = int(input('Oque quer fazer com o numero{} e {}? \n[1] SOMAR: \n[2] MULTIPLICAR: \n[3] DIVIDIR: \n[4] SAIR: \nRESPOSTA: '.format(num1, num2)))
    if resposta == 1:
        x = num1 + num2
        print('A soma de {:.1f} + {:.1f} = {:.2f}'.format(num1, num2, x))
        sleep(1)
        rep = str(input('Deseja continuar? ')).strip().upper()[0]
        sleep(1)
        if rep == 'NAO':
            acertou = True
    elif resposta == 2:
        x = num1 * num2
        print('A multiplicação de {:.1f} * {:.1f} = {:.2f}'.format(num1, num2, x))
        sleep(1)
        rep = str(input('Deseja continuar? ')).strip().upper()[0]
        sleep(1)
        if rep == 'NAO':
            acertou = True
    elif resposta == 3:
        x = num1 / num2
        print('A divisão de {:.1f} / {:.1f} = {:.2f}'.format(num1, num2, x))
        sleep(1) 
        rep = str(input('Deseja continuar? ')).strip().upper()[0]
        sleep(1)
        if rep == 'NAO':
            acertou = True   
    elif resposta == 4:
        acertou = True
        sleep(0.5)
    else:
        print('Erro, digite um valor de 1 a 4!')
        sleep(2)
print('OBRIGADO POR PARTICIPAR!!!')