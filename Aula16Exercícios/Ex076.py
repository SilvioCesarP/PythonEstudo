#Crie uma tupla
#Leia nomes de produtos e o preço
#Mostre uma lista dos preços e nome em tabela

prod = ('lapis', 2, 'borracha', 3, 'penal', 4, 'sunga', 5)
count = 1
print('-#'*19)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-#'*19)
for c in range(0, len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:-<30}', end='')
    else:
        print(f'R${prod[c]:>6.2f}')
print('-#'*19)
    