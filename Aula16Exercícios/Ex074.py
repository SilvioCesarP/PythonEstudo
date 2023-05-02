from random import randint

numeros = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end=' ')
print(f'\nO maior numero dos numeros sorteados é: {max(numeros)}')
print(f'O menor numero dos numeros sorteados é: {min(numeros)}')
