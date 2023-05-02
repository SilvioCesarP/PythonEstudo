#Crie uma tupla com 20 times
#Mostre, os 5 primeiros, os 4 ultimos, os times em ordem alfabéticas e em mque posição está o chapecoense

Times = ('botafogo', 'fortaleza', 'palmeiras', 'internacional', 'cruzeiro', 'grêmio', 'são paulo', 'vasco da gama', 'atlético-MG', 'santos', 'bragantino', 'flamengo', 'athletico-PR', 'bahia', 'goiás', 'corinthians', 'guiabá', 'coritiba', 'américa-MG')
print(f'Os primeiro 5 times do Campeonato Brasileiro de futebol, são:\n{Times[0]}, {Times[1]}, {Times[2]}, {Times[3]} e {Times[4]}')
print(f'E os 4 ultimos times, são:\n {Times[-1]}, {Times[-2]}, {Times[-3]} e {Times[-4]}')
print(f'Os times em ordem alfabéticas são: {sorted(Times)}')
print(f'E o time Flamengo está na posição {Times.index("flamengo")+1}')