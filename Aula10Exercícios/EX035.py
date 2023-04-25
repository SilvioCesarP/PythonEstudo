
#leia 3 lados de um triangulo
#Mostre se esses lados podem ou não formar um triangulo

l1 = float(input('Informe o primeiro lado do triangulo: '))
l2 = float(input('Informe o segundo lado do triangulo: '))
l3 = float(input('Informe o terceiro e ultimo lado do triangulo: '))
maior = l1
menor = l2 + l3
if l2 > l1 and l2 > l3: 
    maior = l2
    menor = l1 + l3
if l3 > l1 and l3 > l1:
    maior = l3
    menor = l1 + l2
if menor > maior:
    print('É um triangulo')
else:
    print('Não é um triangulo')
