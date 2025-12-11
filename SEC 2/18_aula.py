# funcao no caso def 

# 1 - funcao para imprimir uma mensagem 

def welcome():
    print('Bem vindo ao sistema de animes')



# anime list 

animeList1 = ['Solo Leveling', 'Jujutsu Kaisen', 'Atack on Titan', 'Star vs forces of evil']

def animelist():
        global animeList1
        animesWithA = [anime for anime in animeList if 'a' in anime.lower()]
        print(animesWithA)

def animeFilter():
    global animeList1
    filter = 'a'

    anime_Filtred = [
        anime for anime in animeList1
        if anime[0].lower == filter.lower()
    ] 
    print(anime_Filtred)

animeFilter()
