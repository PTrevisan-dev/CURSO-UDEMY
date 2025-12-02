# concatenando valores 

name = input('bskt player of the year\n')
ppg = float(input('points per game\n')) 
fg = int(input('field goal\n'))

print('players stats')
print('=============================')

# alternativa 1 
print(f'Player:{name}')
print(f'Ppg:{ppg}')
print(f'Field goal:{fg}')

# alternativa 2 u tilizando o f'' e o \n

print(f'Player:{name}\n')
print(f'Points per game:{ppg}\n')
print(f'Field goal:{fg}\n')

#alternativa 3

print(f'Player:{name}\n'
      f'Points per game:{ppg}\n'
      f'Field goal:{fg}\n'
      )

