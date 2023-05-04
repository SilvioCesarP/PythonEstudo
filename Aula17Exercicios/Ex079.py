#crie uma lista 
#Pergunte  a cada numero inserido, ao usuario, se ele deseja continuar
#Caso o numero se repita, não adicionar na lista
#Deixar resultado final em ordem crescente
num = []
c = 0

while True:
    n = int(input('Digite um numero: '))
    num.append(n)

    if num.count(n) == 1:
        print('Esse numero foi adicionado com sucesso')
    
    else:
        print('O numero ja existe na lista, portanto não sera adicionado')
        num.remove(n)
    resp = str(input('Deseja continuar a gerar numeros? [S/N]')).upper().strip()[0]
    if resp  == 'N':
        break
num.sort()
print(f'A lista final gerada é {num}')
