#Leia um numero
#Mostre a tabuada do numero
#pergunte se quer mais uma tabuada
#Encerre quando o numero solicitado for negativo

tabuada = 0


while True:
    num = int(input('Digite um numero que quer ver sua tabuada: '))
    count = 0
    if num < 0:
        break
    else:
        while not count == 10:  
            count += 1
            tabuada = num * count
            print(f'{num} * {count} = {tabuada}')
print('fim')
    
