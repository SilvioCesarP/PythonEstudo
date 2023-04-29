#Leia varios numeros inteiros(while True)
#Pre quando o usuario escrever o numero 999
#Mostre quantos numeros foram digitado e a soma deles
count = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    count += 1
    
print(f'A quantidade de numeros digitados foram {count} e a soma deles é {soma} ')