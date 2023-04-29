#Leia um valor inteiro
#Mostre esse valor em cedula
ced1 = 1
ced5 = 5
ced10 = 10
ced20 = 20
ced50 = 50
ced100 = 100
ced200 = 200
resto = 0

valor = int(input('Digite o valor que quer sacar! '))
while True:
    if valor // 200 > 1:
        ced200 = valor // 200
        resto = valor -(ced200*200)
    if valor/100  > 0:
        ced100 = valor / 100
    if valor / 50 == 0:
        ced50 = valor/50
    if valor / 20 == 0:
        ced20 = valor/20
    print(ced200,ced100, ced50, ced20)
    break



