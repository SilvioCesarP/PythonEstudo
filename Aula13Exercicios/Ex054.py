#Leia a data de nascimento de 7 pessoas
#mostre quantas pessoas são maiores de 18 e quantas são menores
from datetime import date
countmaior = 0
countmenor = 0
for pg in range(0, 7):
    nascimento = int(input('Qual a sua data de nascimento? '))
    idade = date.today().year - nascimento
    if idade >= 18:
        countmaior += 1 
    else:
        countmenor += 1
print('Das 7 pessoas {} são menores do que 18 anos e {} são maiores'.format(countmenor, countmaior))


