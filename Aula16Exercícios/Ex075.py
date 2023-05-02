#Leia 4 valores e guarde na tupla
#Quantas vezes apareceu o numero 9,  em que posiçãoo numero 3 está e quais foram os numeros pares

v = (int(input('Digite o valore: ')), 
int(input('Digite o valore: ')), 
int(input('Digite o valore: ')), 
int(input('Digite o valore: ')))
print(v)
print(v.count(9))
if 3 in v:
    print(v.index(3))
else:
    print('Não tem o numero 3')    
for n in v:
    if n % 2 == 0:
        print(n, end=' ')


