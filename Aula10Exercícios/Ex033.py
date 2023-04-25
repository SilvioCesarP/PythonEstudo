#Leia 3 numeros
#Mostre qual é maior e qual é o menor numero dentre eles

a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite outro numero: '))
maior = c
if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b

menor = c
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))



