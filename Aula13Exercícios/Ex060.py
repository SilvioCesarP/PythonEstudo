#Leia um número
#Mostre o fatorial do numero

num = float(input('Digite um numero: '))
x = num
while not x == 1:
    if x == 0:
        x = num
        c = x * num
    else:
    x = (num - 1)
    c = x * num

print(c)


