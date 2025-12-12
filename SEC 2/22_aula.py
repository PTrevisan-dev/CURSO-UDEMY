# fun lambda ---- funcao de potencia de um numero 

power = lambda num: num ** 2

# funcao que verifica se o numero e par 
is_even = lambda x: x % 2 == 0 
print(power(5))
print(power(9))

# funcao que verifica se o numero e impar 
is_odd = lambda x: x % 2 != 0 

# funcao que divide um numero por outro 
div_num = lambda x, y: x / y 

# funcao que reverte uma string 
reverse_strg = lambda s: s[::-1]



print(power(5))
print(power(9))
print(is_even(27))
print(is_even(8))
print(is_odd(18))
print(is_odd(27))
print(div_num(9,3))
print(div_num(3,9))
print(reverse_strg('Python'))
print(reverse_strg('arara'))

# funcionalidade relacionada aos animes:

animeList = ['Solo Leveling', 'Jujutsu Kaisen', 'Atack on Titan', 'Star vs forces of evil', 'Spy Family']
ratings = {
    'Solo Leveling': [8.5, 9.0, 7.5],
    'Jujutsu Kaisen': [8.5, 9.0, 7.5],
    'Atack on Titan': [8.5, 9.0, 7.5],
    'Star vs forces of evil': [8.5, 9.0, 7.5],
}

# funcao para calcular a media de avaliacoes de um anime 
average_rating = lambda anime_name: sum(ratings[anime_name]) / len(ratings[anime_name])

print(f'Media de Avaliacao do anime Solo Leveling: {average_rating('Solo Leveling'):.1f}')

# funcao que verifica se um anime esta na lista 
check_anime = lambda anime_name: anime_name in animeList

print(f'Solo Leveling esta na lista {check_anime('Solo Leveling')}')

# funcao para recomendar o filme com base na avaliacao do filme 

recomended_anime = lambda anime_name: f'Recomendo {anime_name} com meida de {average_rating(anime_name):.1f}'
print(recomended_anime('Solo Leveling'))