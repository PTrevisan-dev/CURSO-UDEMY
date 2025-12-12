# metodos para listas 

filmlist = ['Kung fu panda', 'Interstellar', 'Intocaveis', 
            'star vs forças do mal']
        
# 1- tamanho da lista 
print(len(filmlist))

# 2- recuperar um iten da lista pelo nome 
print(filmlist.index('star vs forças do mal'))

# 3- adicionar item ao final da lista
filmlist.append('Game of Thrones')
print(filmlist)

# 4- ordenas lista 
filmlist.sort()
print(filmlist)

# 5- copiar um filme de uma lista para outra 
filmcopy = filmlist.copy()
filmcopy.remove('Interstellar')
print(filmcopy)

# 6- remover tudo da lista 
filmlist.clear()
print(filmlist)