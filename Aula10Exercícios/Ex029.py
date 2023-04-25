
#Leia a velocidade de um carro
#Se a velocidade passar de 80, mostrar multa
#Multa sera cobrado 7 reais a cada km rodado acima da velocidade

velocidade = int(input('Digite sua velocidade: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Voce ultrapassou a velocidade permetida de 80km, recebendo uma multa de {}'.format(multa))
else:
    print('Parabens por passar na velocidade permitida!')
