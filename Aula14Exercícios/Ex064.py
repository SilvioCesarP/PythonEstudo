#Leia vários numeros inteiros
#Para o programa quando for digitado 999
#Mostre quantos numeros foram digitados e qual a soma deles
num = 0
count = 1
n1 = 0
n2 = 0

while num != 999:
        n2 = n1
        num = int(input(f'Digite o {count}º numero[Digite 999 para parar]: '))       
        n1 = num + n2
        count += 1
print(f'Foi usado {count - 2} numeros e a soma total deles é {n2}')    