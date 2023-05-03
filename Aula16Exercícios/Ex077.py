#Criei varias palavras em um tupla
#Mostre mais avogais estão presentes nessas palavras

palavra = ('raio', 'mitigar', 'zeus', 'orintorinco', 'portifolio', 'sabonete', 'palavras', 'reuniao', 'coragem', 'situacao')

for c in palavra:
    print(f'\nA palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')
