#Leia um número
#Mostre o fatorial do numero

num = float(input('Digite um numero: '))
x = num
fac = 1
while x > 1:
         fac = x * fac
         x = x - 1
print('O fatorial de {:.2f} é {:.2f}'.format(num, fac))
