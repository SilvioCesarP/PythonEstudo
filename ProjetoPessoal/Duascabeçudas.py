#3 individuo(galinha, lobo, vaca)
#Perguntarqual passa primeiro
#não pode deixar o lobo sozinho com nem umas das duas, galinha ou vaca


print('BEM VINDO AO JOGUINHO DO SILVIO')
print('-='* 20)
print('VOCE É AMIGO DE TODOS OS ANIMAIS, E CUIDA DE UM LOBO, UMA VACA E UMA GALINHAZ\nPOREM PRECISA IR NA CIDADE COMPRAR COMIDA POIS SEU LOBO ESTA MORRENDO DE FOME')
print('PARA CHEGAR NA CIDADE PRECISA ATRAVESAR UM RIO, VOCÊ SÓ TEM UM BOTE QUE CABE APENAS 2 PASSAGEIROS\nSE DEIXAR O LOBO SOZINHO COM A VACA OU A GALINHA ELE VAI COMER ELAS :C')
print('Sendo você o unico que consegue dirigir o bote, vamos considerar cada um com um numero\nLOBO[1]\nGALINHA[2]\nVACA[3]\nVOCE[4]')

morreu = 1
while True:
    if morreu == 0:
        break
    resp1 = int(input('QUAL ANIMAL ATRAVESSERA PRIMEIRO?[1, 2, 3]: '))
    if resp1 == 2 == 3:
        print('NÃOOOO, VOCE DEIXOU O LOBO SOZINHO COM OS ANIMAIS, ELE COMEU ELES DE TANTA FOME!!!')
        break     
    elif resp1 == 1:
        while True:
            if morreu == 0:
                break
            print('Otimo, agora tem um lobo do outro lado e a galinha e a vaca deste lado')
            resp2 = int(input('QUAL ANIMAL ATRAVESSERÁ?'))
            
            if resp2 == 2:
                while True:
                    print('Otimo, agora tem um LOBO e uma GALINHA de um lado e uma VACA do outro')
                    resp3 = int(input('QUAL ANIMAL ATRAVESSERÁ?'))
                    if resp3 == 3:
                        print('NÃOOOO, VOCE DEIXOU O LOBO SOZINHO COM OS ANIMAIS, ELE COMEU ELES DE TANTA FOME!!!')
                        morreu = 0
                        break
                    if resp3 == 1:
                        print('Voce moveu o LOBO junto a GALINHA, deixando a VACA do outro lado')
                    if resp3 == 2:
                        break
            if resp2 == 3:
                print('Otimo, agora tem um LOBO e uma VACA de um lado e uma GALINHA do outro')
            if resp2 == 1:
                resp = 1
print('FIM')                   

            
        
            




    