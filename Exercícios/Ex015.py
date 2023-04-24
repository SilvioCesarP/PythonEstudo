#Perguntar 2 variaveis, KM e tempo
#Depois calcular o quanto custou sendo que 60 R$ por tempo e 0,15R$ por km percorido
km = float(input('Quantos KM percorreu com o carro alugado? '))
tempo = float(input('Por quanto tempo voce alugou o carro? '))
aluguel = (60 * tempo) + (km * 0.15)
print('O aluguel do seu carro ficou: {}'.format(aluguel))