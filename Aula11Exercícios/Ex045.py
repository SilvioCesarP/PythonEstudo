#Crie o jogo jokenpo
#leia umas das 3 opçoes 
#gere um numero de 1 a 3
#Mostre o resultado

import random
from time import sleep

print(''' ESCOLHA UMA DAS OPÇOES: 
[ 0 ] PEDRA:
[ 1 ] PAPEL:
[ 2 ] TESOURA:''')
item = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0,2)
escolha = int(input('QUAL OPÇÃO ESCOLHERA? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('=-' * 20)
print('O COMPUTADOR ESCOLHEU {}'.format(item[pc]))
print('O JOGADOR ESCOLHEU {}'.format(item[escolha]))
print('=-' * 20)
if escolha == pc:
    print('EMPATE!!!')
elif escolha == 0 and pc == 1:
    print('VOCÊ PERDEU!!!')
elif escolha == 1 and pc == 0:
    print('GANHOU!!!')
elif escolha == 2 and pc == 1:
    print('GANHOU!!!')
elif escolha == 0 and pc == 2:
    print('GANHOU!!!')
elif escolha == 1 and pc == 2:
    print('VOCÊ PERDEU!!!')
elif escolha == 2 and pc == 0:
    print('VOCÊ PERDEU!!!')
else:
    print('Escolha uma opção viavel!!!')
