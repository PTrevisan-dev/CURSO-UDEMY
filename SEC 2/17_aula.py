# list comprehension 

# 1- listando valores de 0 a 10 que sejam maiores do que 4

listNumbersplus4 = [i for i in range(10) if i > 4]
print(listNumbersplus4)
'''
usando o FOR
for i in range(10): 
    if i > 4:
        print(i)
'''
# listando valores de 0 a 10 que sejam menores do que 4

listNumbersminus4 = [i for i in range(10) if i < 4]
print(listNumbersminus4)

'''
usando o FOR 
print i in range(10):
    if i < 4:
        print(i)
'''


# da para fazer por exemplo um sistema de entrada de roupas com os nomes, modelos 
# e depois procurar no sistema pelo numero ou nome ou primera letra 
# lista de animes 
animeList = ['Solo Leveling', 'Jujutsu Kaisen', 'Atack on Titan', 'Star vs forces of evil']

# animes que possuem a letra 'o' mo titulo 

animesWithO = [anime for anime in animeList if 'O' in anime.upper()]
print(animesWithO)

# controle do que ainda falta ou do que ja tem 
# animes que eu assisti 
animesWatched = [anime for anime in animeList if anime != 'atack on titan'] 
print(animesWatched)

# encontrando um filme pelo nome 
while True :
    searchName = input('digite o nome do anime para buscar na lista (ou digite sair para encerrar):\n')
    if searchName.lower() == 'sair':
        print('programa encerrado')
        break

    foundAnimes = [anime for anime in animeList if searchName.lower() in anime.lower()]
    if foundAnimes:
        print(f'Anime(s) encontrado(s) com o nome:{searchName}')
        for foundAnimes in foundAnimes :
            print(foundAnimes)
    else:
        print('Filme não encontrado')
