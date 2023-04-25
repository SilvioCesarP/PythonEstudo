#Leia um número de 1 a 9999
#Mostre cada digito e seus valores

num = int(input('Digite um numero de 1 a 9999: '))


if num >= 0000 and num <= 9999:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('No seu numero {} tem; \n Unidade:{} \n Dezena:{} \n Centena:{} \n Milhar: {}'.format(num, u, d, c, m))


 
