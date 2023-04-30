#3 individuo(galinha, lobo, vaca)
#Perguntarqual passa primeiro
#não pode deixar o lobo sozinho com nem umas das duas, galinha ou vaca


print('BEM VINDO AO JOGUINHO DO SILVIO')
print('-='* 20)
print('VOCE É AMIGO DE TODOS OS ANIMAIS, E CUIDA DE UM LOBO, UMA VACA E UMA GALINHAZ\nPOREM PRECISA IR NA CIDADE COMPRAR COMIDA POIS SEU LOBO ESTA MORRENDO DE FOME')
print('PARA CHEGAR NA CIDADE PRECISA ATRAVESAR UM RIO, VOCÊ SÓ TEM UM BOTE QUE CABE APENAS 2 PASSAGEIROS\nSE DEIXAR O LOBO SOZINHO COM A VACA OU A GALINHA ELE VAI COMER ELAS :C')
print('VOCE SENDO O UNICO QUE CONSEGUE DIRIGIR A CANOA, ESCOLHA ')
n1 = 'LOBO'
n3 = 'VACA'
n2 = 'GALINHA'
jogada = (('QUAL ANIMAL ATRAVESSERÁ?\n{}[1]\n{}[2]\n{}[3]\nRESPOSTA: '))
perdeu = 'NÃOOOO, VOCE DEIXOU O LOBO SOZINHO COM OS ANIMAIS, ELE COMEU ELES DE TANTA FOME!!!'
morreu = 1


while True:
    R1 = int(input((jogada).format(n1, n2, n3)))
    if morreu == 0:
        break
    elif R1 == 2 or R1 == 3:
        print((perdeu))
        break
    elif R1 == 1:
        n1 = 'LOBO'
        n2 = 'GALINHA'
        n3 = 'VACA'
        while True:
            print(f'Apos a travessia temos:{n1} de um lado e do outro a {n2} junto com a {n3}')
            R2 = int(input((jogada).format(n1, n2 ,n3)))
            if morreu == 0:
                break
            if R2 == 1:
                break
            if R2 == 3 or R2 == 2:
                while True:
                    if R2 == 2:
                        n1 = 'LOBO'
                        n2 = 'GALINHA'
                        n3 = 'VACA'
                    elif R2 == 3:
                        n1 = 'LOBO'
                        n2 = 'VACA'
                        n3 = 'GALINHA'
                    print('Apos a travessia temos:{n1} e {n2} junto, e {n3} do outro')
                    n1 = 1
                    n2 = 2
                    n3 = 3 
                    R3 = int(input(jogada))
                    if morreu == 0:
                        break
                    if R2 == 2:
                        break




