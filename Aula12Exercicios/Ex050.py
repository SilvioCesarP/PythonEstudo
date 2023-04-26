#Leia seis numeros inteiros
#Mostre apenos os numeros pares
soma = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += + n
        count += + 1
print('voce informou {} numeros PARES e a soma é {}'.format(count, soma))