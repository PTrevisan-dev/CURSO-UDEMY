# for loop

movielist = ['solo leveling', 'jujutsu kaisen', 'atack on titan', 'star vs forces of evil']

# 1 - interar valores de uma lista 

for movie in movielist:
    print(movie)

# 2 - usar o break 

for movie in movielist:
    if movie == 'atack on titan':
        break
print(movie)

# 3 - usar o continue 

for movie in movielist:
 if movie == 'atack on titan':
    continue

# 4 - avaliação de um filme :

animeName = input('digite o nome do filme :\n')
animerating = int(input('Digite qunatas avaliações desja fazer:\n'))

total = 0 
for i in range(animerating):
    note = float(input('Digite a nota para o filme:\n'))
    total += note 

if animerating > 0:
    average = total / animerating
else:
    average = 0 

print(f'A média de avaliação do filme {animeName} é: {average:.2f}')
