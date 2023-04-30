#3 individuo(galinha, lobo, vaca)
#Perguntarqual passa primeiro
#não pode deixar o lobo sozinho com nem umas das duas, galinha ou vaca


print('BEM VINDO AO JOGUINHO DO SILVIO')
print('-='* 20)
print('VOCE É AMIGO DE TODOS OS ANIMAIS, E CUIDA DE UM LOBO, UMA VACA E UMA GALINHAZ\nPOREM PRECISA IR NA CIDADE COMPRAR COMIDA POIS SEU LOBO ESTA MORRENDO DE FOME')
print('PARA CHEGAR NA CIDADE PRECISA ATRAVESAR UM RIO, VOCÊ SÓ TEM UM BOTE QUE CABE APENAS 2 PASSAGEIROS\nSE DEIXAR O LOBO SOZINHO COM A VACA OU A GALINHA ELE VAI COMER ELAS :C')
print('Sendo você o unico que consegue dirigir o bote, vamos considerar cada um com um numero\nLOBO[1]\nGALINHA[2]\nVACA[3]\nVOCE[4]')
jogada = 'QUAL ANIMAL ATRAVESSERÁ?\n LOBO[1]\nGALINHA[2]\nVACA[3]\nRESPOSTA: '
perdeu = 'NÃOOOO, VOCE DEIXOU O LOBO SOZINHO COM OS ANIMAIS, ELE COMEU ELES DE TANTA FOME!!!'
morreu = 1

while True:
    if morreu == 0:
        break
    resp1 = int(input('QUAL ANIMAL ATRAVESSERA PRIMEIRO?[1, 2, 3]: '))
    if resp1 == 2 == 3:
        print(perdeu)
        break     
    elif resp1 == 1:
        while True:
            if morreu == 0:
                break
            print('Otimo, agora tem um LOBO de um lada e a GALINHA e a VACA do outro lado')
            resp2 = int(input(jogada))
            if resp2 == 2 == 3:
                if resp2 == 2:
                    n1 = 'LOBO'
                    n2 = 'GALINHA'
                    n3 = 'VACA'
                elif resp2 == 3:
                    n1 = 'LOBO'
                    n2 = 'VACA'
                    n3 = 'GALINHA'
                while True:
                    print('Otimo, agora tem um {n1} e uma {n2} de um lado e uma {n3} do outro')
                    resp3 = int(input(jogada))
                    if resp3 == 3:
                        print(perdeu)
                        morreu = 0
                        break
                    if resp3 == 1:
                        print('Voce moveu o LOBO junto a GALINHA, deixando a VACA do outro lado')
                    if resp3 == 2:
                        break
        
            if resp2 == 1:
                break



print('FIM')                   

            
        
            




    