#Leia um numero = n
#Mostre a sequencia de bibonacci até o n x

n = int(input('Digite um numero: '))
count = 0
t1 = 0
t2 = 1
t3 = t1 + t2
print(f'{t1} -> {t2}', end='')

while count != n:
    count += 1
    t3 = t2 + t1

    print(f' -> {t3}', end='')
    
    t1 = t2
    t2 = t3

print('FIM')
    
