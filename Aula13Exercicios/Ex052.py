#Leia um numero
#Mostre se esse numero é ou não um numero primo

num = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('O numero {} foi repetido {} vezes'.format(num, tot))
if tot == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')        
   

