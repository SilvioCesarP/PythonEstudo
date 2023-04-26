#Mostre a soma de todos os numero impares que são multiplos de 3 do 1 a 500
soma = 0
count = 0
for c in range(1 , 501, 2):
    if c % 3 == 0:
        count += + 1
        soma  += + c
print('A soma dos {} valores é {}'.format(count, soma))
