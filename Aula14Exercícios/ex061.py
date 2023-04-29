#Leia o primeiro termo e a razão de uma pa 
#Mostre os 10 primeiros termos
print('GERADOR DE PA')
print('=-'*20)
num = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
c = num
while c < num + (razao * 10):
        if c == num:
            c = num
            print(c, end=', ')
            c += razao
        else:
            c += razao
            print(c, end= ', ')
print('o PA do numero {} na razão de {} nos primeiros 10 termos'.format(num, razao))
        
