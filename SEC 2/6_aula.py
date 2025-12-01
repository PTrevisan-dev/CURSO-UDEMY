#slice 

movie = 'top gun'
# strinng [inicio:fim] - índice começa na posição 0 / índice final -1 

# 1 - buscar toda a string a partir da primeira posição 
print(movie[0:])

# 2 - buscar toda a string até a ultima posição 
print(movie[:7]) # ele conta espaçamentos 

# 3 - buscar toda a string a partit da  terceira posição 
print(movie[2:]) # lembrar sempre que começa pelo 0 

''' 
strinng [inicio:fim]
índice começa na posição 0 / índice final -1
passo - determina o incremento. Por padrão esse numero é 1.  no caso seria de quanto em quanto isso vai 
'''
# 4 - Buscar toda a str de 2 em 2 caracteres 
print(movie[::2])

# 5 - Buscar toda a str nos indices impares
print(movie[1::2])

# 6 - inverter uma str de tras para frente 
print(movie[::-1])




