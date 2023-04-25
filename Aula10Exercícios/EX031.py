#Leia a distancia de uma viagem
#calcule o preço da passagem sendo 0,50 reais para viagem menores de 200km e 0,45 reais para maiores

km = float(input('Quantos KM voce percorerá? '))
p1 = km * 0.50
p2 = km * 0.45
if km < 200:
    print('Sua viagem é curta, sendo cobrado apenas 0,30 por km rodado, resultando em R${:.2f} a passagem'.format(p1))
else:
    print('Sua viagem é longa. sendo cobrado 0,45 por km rodado, resultando em R${:.2f} a passagem'.format(p2))