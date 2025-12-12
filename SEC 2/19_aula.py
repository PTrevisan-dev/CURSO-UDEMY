# agrs em func.  ---------- colocar as coisas no parenteses da func


# 1 - funcao para imprimir nome completo

def full_name(first_name, last_name):
    print(f'Nome e: {first_name} {last_name}')


full_name('Pedro', 'Trevisan')

# 2 - funcao para somar dois numeros 

def sum_numbers(a, b):
    return a + b 

print(f'A soma e: {sum_numbers(10, 50)}')


# 3 - funcao com parametro default 

def address(country = 'Brasil'):
    print(f'Eu moro em : {country}')

address() # nao entendi o pq alguem faria algo com parametros 

# 4 - funcao para avaliar o filme 
def rate_movie(num_rating, anime_name):
    total = 0
    for i in range(num_rating):
        note = float(input('Digite a nota para o anime:\n'))
        total += note 

    if num_rating > 0:
            average = total / num_rating
    else:
            0
    print(f'Media de avaliacao do anime: {anime_name} e: {average:.1f}')

rate_movie(2, 'Solo leveling')            