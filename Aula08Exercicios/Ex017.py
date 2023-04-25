#Leia o comprimento do cateto oposto e do adjecente de um triangulo
#E calcule o comprimento da hipotenusa
import math
co = float(input('Digite o comprimento do catete oposto: '))
ca = float(input('Digite o cmprimento do cateto adjecente: '))
hi = math.hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.3f}'.format(hi))