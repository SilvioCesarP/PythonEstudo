#Leia um nome de uma cidade
#Mostre se ela começa com a palavra 'Santo'

cidade = str(input('Digite o nome da sua cidade ou alguma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')


