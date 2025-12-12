# lista de filmes 


animeList = ['solo leveling', 'jujutsu kaisen', 'atack on titan', 'star vs forces of evil']

# 1 - interando valores de uma lista de filmes usando While 

index = 0 
while index < len(animeList):
    print(animeList[index])
    index += 1

# 2 - quando a condicção for atendida o loop encerra (Break)

index = 0 
while index < len(animeList):
    if animeList[index] == 'atack on titan':
        break
    print(animeList[index])
    index += 1

# 3 - quando a condição for atendida o loop vai para a proximainteração

index = 0 
while index < len(animeList):
    if animeList[index] == 'atack on titan':
        continue
    print(animeList[index])
    index += 1 

# 4 - avaliação do filme com while 

animeRating = float(input('Digite quantas avaliações deseja fazer:'))
animeName = input('Digite o nome do anime :')

total = 0 
count = 0 

while count < animeRating:
    note = float(input('Digite a nota do anime:'))
    total += note 
    count += 1 

if animeRating > 0:
    average = total / animeRating     
else:
    average =0 

print(f'A média de avaliação do filme {animeName} é: {average:.2f}')