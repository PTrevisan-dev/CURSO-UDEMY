# funcao no caso def 

# 1 - funcao para imprimir uma mensagem 

def welcome():
    print('Bem vindo ao sistema de animes')

# 2 - repetindo a funcao 
#for i in range(10):
#     welcome

# 3 - funcao para calcular a media de notas 

def average_calc(): 
     
     average_num1 = int(input('Quantas avaliacoes deseja fazer ? :\n'))
     total = 0 
     for i in range(average_num1):
          note = float(input('Digite a nota para o(s) anime(s):\n'
                             '>'))
          total += note
    
     if average_num1 > 0:
         average = total / average_num1
         return average
     else:
          0
    
print(f'A media das avaliacoes e: {average_calc():.2f}')



def create_anime():
     name = input('Digite o nome do anime:\n')
     yearLaunch = int(input('Digite o ano de lancamento:\n'))
     anime_price = float(input('Digite o valor do anime / manga: \n'))
     anime_rating = float(input('Digite a nota de avaliacao do anime:'))
     print(f'{name} ({yearLaunch}) - R$ {anime_price} {anime_rating:.f1}')


create_anime()    

# anime list 

animeList1 = ['Solo Leveling', 'Jujutsu Kaisen', 'Atack on Titan', 'Star vs forces of evil']

def animelist():
        global animeList1
        animesWithA = [anime for anime in animeList1 if 'a' in anime.lower()]
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

