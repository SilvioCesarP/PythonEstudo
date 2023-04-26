#Leia 3 lados de um triangulo
#Mostre se o triangulo formado é equilátero, isóseles ou escaleno

l1 = float(input('Digite o comprimento de um lado do triangulo: '))
l2 = float(input('Digite o comprimento de outro lado do triangulo: '))
l3 = float(input('Digite o ultimo comprimento do triangulo: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l2 + l1:
    print('Parabens! Seu triangulo está formado e é: ')
    if l1 == l2 == l3:
        print('Um trigulo EQUILÁTERO!!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Um triangulo ISÓCELES!!')
    else:
        print('Um triangulo ESCALENO!!')
else: 
    print('Infelizmente não pode formar um triangulo com esses comprimentos!')



