class game:
    name = ''
    yearlunch = 0
    mp = False 
    note = 0

# primeiro jogo 

game1 = game()
game1.name = ' the legend of zelda'
game1.yearlunch = 2017
game1.mp = False 
game1.note = 9.7

# segundo jogo 

game2 = game()
game2.name = 'fortnite'
game2.yearlunch = 2017
game2.mp = True
game2.note = 9.0

print('###Dados do Jogo')
print(f'Nome do jogo: {game1.name}\nMulti Player: {game1.note}')
print(f'Nome do jogo: {game2.name}\nMulti Player: {game2.mp}')