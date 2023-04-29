#Leia um primeiro termos(numero) e a razão de uma PA
#Mostre os 10 primeiros termos

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de PA: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print( c, end='->')

print('ACABOU')
