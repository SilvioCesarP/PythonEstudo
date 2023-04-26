#leia um numero
#Faça uma tabuada com ele
#Mostre a tabuada utilizando laço for
num = int(input('Digite um numero: '))
k = 0
for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, num * c))
