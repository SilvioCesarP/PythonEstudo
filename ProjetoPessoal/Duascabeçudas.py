#3 individuo(galinha, lobo, vaca)
#Perguntarqual passa primeiro
#não pode deixar o lobo sozinho com nem umas das duas, galinha ou vaca


print('BEM VINDO AO JOGUINHO DO SILVIO')
print('-='* 20)
print('VOCE É AMIGO DE TODOS OS ANIMAIS, E CUIDA DE UM LOBO, UMA VACA E UMA GALINHAZ\nPOREM PRECISA IR NA CIDADE COMPRAR COMIDA POIS SEU LOBO ESTA MORRENDO DE FOME.')
print('PARA CHEGAR NA CIDADE PRECISA ATRAVESAR UM RIO, VOCÊ SÓ TEM UM BOTE QUE CABE APENAS 2 PASSAGEIROS\nSE DEIXAR O LOBO SOZINHO COM A VACA OU A GALINHA ELE VAI COMER ELAS :C')
print('VOCE SENDO O UNICO QUE CONSEGUE DIRIGIR A CANOA, ESCOLHA ')
n1 = [1, 'LOBO']
n3 = [2, 'VACA']
n2 = [3, 'GALINHA']
jogada = (('QUAL ANIMAL ATRAVESSERÁ?\n{}[1]\n{}[2]\n{}[3]\nRESPOSTA: '))
perdeu = 'NÃOOOO, VOCE DEIXOU O LOBO SOZINHO COM OS ANIMAIS, ELE COMEU ELES DE TANTA FOME!!!'
morreu = 1
reset = 0
vitoria = 0

while True:
    if morreu == 0 or vitoria == 1:
        break      
    if reset == 1:
        reset = 0
    print(f'Temos a seguinte situação: o {n1[1]}, a {n2[1]} e a {n3[1]}, e claro VOCÊ!')
    R1 = int(input((jogada).format(n1[1], n2[1], n3[1])))
    if R1 == 2 or R1 == 3:
        morreu = 0
        print((perdeu))
        break
    elif R1 == 1:
        n1 = [1,'LOBO']
        n2 = [2, 'GALINHA']
        n3 = [3, 'VACA']
        while True:
            if morreu == 0 and reset == 1 or vitoria == 1:
                break
            print(f'Apos1 a travessia, temos:{n1[1]} de um lado e do outro a {n2[1]} junto com a {n3[1]}')
            R2 = int(input((jogada).format(n1[1], n2[1] ,n3[1])))
            if R2 == 1:
                break
            if R2 == 3 or R2 == 2:
                while True:
                    if morreu == 0 and reset == 1 or vitoria == 1:
                        break
                    if R2 == 2:
                        n1 = [1, 'LOBO']
                        n2 = [2, 'GALINHA']
                        n3 = [3, 'VACA']
                    elif R2 == 3:
                        n1 = [1, 'LOBO']
                        n2 = [3, 'VACA']
                        n3 = [2, 'GALINHA']
                    print(f'Apos2 a travessia, temos:{n1[1]} e {n2[1]} juntos e a {n3[1]} do outro lado')
                    R3 = int(input((jogada).format(n1[1], n2[1], n3[1])))#feito
                    if R3 == 2:
                        break
                    elif R3 == 3:
                        morreu = 0
                        print(perdeu)
                        break
                    elif R3 == 1:
                        while True:
                            if morreu == 0 or vitoria == 1:
                                 break
                            print(f'Apos3 a travessia, temos: {n2[1]} de um lado e no outro o {n1[1]} e a {n3[1]}')
                            resp4 = int(input((jogada).format(n1[1], n2[1], n3[1])))
                            if resp4 == 2:
                                morreu = 0
                                print(perdeu)
                                break
                            if resp4 == 1:
                                break
                            if resp4 == 3:
                                while True:
                                    print(f'Apos4 a travessia, temos:{n2[1]} e {n3[1]} de um lado e {n1[1]} do outro')
                                    resp5 = int(input((jogada).format(n1[1], n2[1], n3[1])))
                                    if resp5 == n2[0] or resp5 == n3[0]:
                                        break
                                    elif resp5 == n1[0]:
                                        print('PARABENS!!')
                                        vitoria = 1
                                        break
                           
print('FIM')

                            



                        




