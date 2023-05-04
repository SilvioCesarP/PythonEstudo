#Leia 5 valores e coloque em uma lista
#Mostre a lista e quais valores foram maiores e quais foram menores e suas posiçoes

num = []
maior = menor = 0


for c in range(0, 5):
    num.append(int(input('Digite um numero: ')))
    if c == 0:
        maior = menor = num[c]
    elif num[c] > maior:
        maior = num[c]
    elif num[c] < menor:
        menor = num[c]
    




print(f'Os numeros da lista são: {num}')

print(f'O numero maior desta lista é {maior}', end='')
for i , v in enumerate(num):
    if v == maior:
        print(f' e a posição é {i}')
print(f'O numero menor desta lista é {menor}')
for i, v in enumerate(num):
    if v == menor:
        print(f' e a posição é {i}')