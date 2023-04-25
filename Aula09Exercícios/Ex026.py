#Leia um frase
#Mostre quantas vezes a letra 'A' aparece
#Mostre em que posição ela aparece pela primeira vez
#Mostre em que posição ela aparece pela ultima vez

frase = str(input('Digite um frase: ')).strip()
fr = frase.upper()
print('A letra A aparece {}'.format(fr.count('A')))
print('A primeira vez a que a letra A aparece é na posição {}'.format(fr.find('A') + 1))
print('A ultima vez que a letr A apareceu é na posição {}'.format(fr.rfind('A')))