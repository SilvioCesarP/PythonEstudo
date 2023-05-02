#Leia um valor inteiro
#Mostre esse valor em cedula

ced = 50
count = 0

valor = int(input('Digite o valor que quer sacar! '))
total = valor
while True:
    if total >= ced:
        total -= ced
        count += 1
    else:
        if count > 0:
            print(f'Voce recebe {count} cédulas de {ced}')
            count = 0
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break

print('Obrigado por usar o melhor banco da cidade')


