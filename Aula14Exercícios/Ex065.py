#Leia varios valores e ao final de cada valor pergunte se quer continuar
#Mostre a média de todos os valores e qual foi o maior e o menor valor lido

resposta =  'S'
count = soma = media = num = maior = menor =  0
while resposta in 'Ss':
    
    num = int(input('Digite um número: '))
    count += 1
    soma += num
    if count == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        elif num <= menor:
            menor = num
    resposta = str(input('Voce ainda quer continuar a gerar novos numeros? [Digite SIM/NAO]: ')).strip().upper()[0] 
media = soma / count
print(f'a média de todos os valores é {media}, e o menor e o maior numero deles é {menor, maior}, respectivamente, e a soma deles é {soma}')

        
         