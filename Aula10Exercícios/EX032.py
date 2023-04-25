
#Leia um ano
#Mostre se ele é bissexto ou não
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
   print('O ano atual é {}'.format(date.today().year))

elif ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
   print('Esse ano é Bissexto!')
else:
   print('Esse ano não é Bissexto!')