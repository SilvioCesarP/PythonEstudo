#Leia dois numeros
#Mostre qual é maior e qual é menor

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n2 > n1:
   print('O numero maior é {} e o menor é {}'.format(n2, n1))
elif n1 > n2:
    print('O numero maior é {} e o menor é {}'.format(n1, n2))
else:
    print('Os dois numeros são igual, assim não existindo maiores ou menores')

