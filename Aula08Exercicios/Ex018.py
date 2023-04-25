#Leia um agulo e dê o valor dele em seno, cosseno e tangente
import math
an = float(input('Digite um angulo: '))
rad = math.radians(an)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O angulo escolido {:.2f}, tem : \n Seno :{:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(an, sen, cos, tan))


