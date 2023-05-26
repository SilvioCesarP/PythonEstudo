#Leia um numero e a opção do jogador(impar ou par)
#Gere um numero aleatório
#Compare o numero escolhido com o numero aleatorio
#Mostre se perdeu ou ganhou
#Conte as vitorias consecutivas e so pare quando o jogador perder

import random
count = 0
while True:
    print('-='*20)
    num = int(input('Digite um numero: '))
    print('-='*20)
    gerado = random.randint(0, 10)
    escolha = ' '
    count += 1
    modulo = (num + gerado) % 2 
    soma = num + gerado
    while escolha not in 'PI':
        escolha = str(input('Escolha ÍMPAR OU PAR [I/P]: ')).upper().strip()[0]
        print('-='*20)
    if modulo == 0 and escolha == 'P':
        print(f'O computador escolheu {gerado} e você {num} somado deu {soma}, numero PAR')
        print(f'PARABENS VC GANHOU! SENDO SUA {count}º VITÓRIA CONSECUTIVA')
    elif modulo == 1 and escolha == 'I':
        print(f'O computador escolheu {gerado} e você {num} somado deu {soma}, numero IMPAR')
        print(f'PARABENS VC GANHOU! SENDO SUA {count}º VITÓRIA CONSECUTIVA')
    else:
        print(f'VOCE PERDEU PARA O COMPUTADOR!!!')
        break
print(f'NUM TOTAL DE {count} VITÓRIA CONSECUTIVAS')
