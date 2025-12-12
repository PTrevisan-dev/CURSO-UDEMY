# set

filmlist = {'Kung fu panda', 'Interstellar', 'Intocaveis', 
            'star vs forças do mal'}

print(type(filmlist))

# 1- buscar tamanho 
print(len(filmlist))

# 2- true e 1 são considerados o mesmo valor 
exampleset = {'inception', True, 1, 8.7}

# 3- adicionar item de outro set 
filmlist.update(exampleset)
print(filmlist)

# 4- remover um item no set 
filmlist.remove(True)
filmlist.remove(8.7)
print(filmlist)
